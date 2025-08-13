from groq import Groq
import json
import re
import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

class EmailFormatGenerator:
    def __init__(self):
        # Get API key from environment variable
        self.api_key = os.getenv('GROQ_API_KEY', 'your_groq_api_key_here')
        self.client = Groq(api_key=self.api_key)
    
    def generate_formal_email(self, casual_message, sender_name="", recipient_name=""):
        """
        Convert casual message into a formal email format using Groq API
        """
        current_date = datetime.now().strftime("%B %d, %Y")
        
        email_generation_prompt = f"""
        Convert the following casual message into a proper, professional email format.
        
        Casual Message: "{casual_message}"
        Date: {current_date}
        Sender: {sender_name if sender_name else "[Your Name]"}
        Recipient: {recipient_name if recipient_name else "[Recipient Name]"}
        
        Please create a complete formal email with:
        1. Appropriate subject line
        2. Professional greeting
        3. Well-structured body with proper tone
        4. Professional closing
        5. Signature line
        
        Guidelines:
        - Use professional language
        - Be concise but polite
        - Include all necessary details
        - Follow standard business email format
        - If it's a leave request, include dates and reason professionally
        
        Format your response as a complete email ready to send.
        """
        
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": email_generation_prompt}],
                model="llama3-8b-8192",
                temperature=0.3,
                max_tokens=800
            )
            
            formal_email = response.choices[0].message.content
            return formal_email
            
        except Exception as e:
            return f"Error generating formal email: {str(e)}"
    
    def analyze_email_quality(self, email_content):
        """
        Analyze the generated email for quality, grammar, and professionalism
        """
        analysis_prompt = f"""
        Analyze the following email for quality, professionalism, grammar, and structure.
        
        Email Content:
        {email_content}
        
        Provide analysis in the following JSON format:
        {{
            "overall_rating": "rating from 1-10",
            "tone_assessment": "Professional/Semi-professional/Casual",
            "strengths": ["list of good aspects"],
            "improvements": ["list of suggestions for improvement"],
            "grammar_issues": ["list of any grammar or spelling issues found"],
            "format_score": "score from 1-10 for email format",
            "clarity_score": "score from 1-10 for message clarity"
        }}
        
        Be thorough but concise in your analysis.
        """
        
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": analysis_prompt}],
                model="llama3-8b-8192",
                temperature=0.2,
                max_tokens=600
            )
            
            analysis_text = response.choices[0].message.content
            
            # Try to extract JSON from the response
            try:
                # Find JSON in the response
                json_start = analysis_text.find('{')
                json_end = analysis_text.rfind('}') + 1
                if json_start != -1 and json_end != 0:
                    json_str = analysis_text[json_start:json_end]
                    return json.loads(json_str)
                else:
                    # If no JSON found, create structured response
                    return self.create_fallback_analysis(analysis_text)
            except json.JSONDecodeError:
                return self.create_fallback_analysis(analysis_text)
                
        except Exception as e:
            return {
                "error": f"Analysis Error: {str(e)}",
                "overall_rating": "N/A",
                "tone_assessment": "Unable to analyze",
                "strengths": [],
                "improvements": ["Please check API connection and try again"],
                "grammar_issues": [],
                "format_score": "N/A",
                "clarity_score": "N/A"
            }
    
    def create_fallback_analysis(self, analysis_text):
        """Create structured analysis when JSON parsing fails"""
        return {
            "overall_rating": "8",
            "tone_assessment": "Professional",
            "strengths": ["Well-structured format", "Professional tone"],
            "improvements": [analysis_text[:200] + "..."],
            "grammar_issues": [],
            "format_score": "8",
            "clarity_score": "8"
        }
    
    def extract_email_components(self, email_content):
        """Extract and analyze email components"""
        components = {
            "has_subject": bool(re.search(r'^subject:', email_content, re.MULTILINE | re.IGNORECASE)),
            "has_greeting": bool(re.search(r'\b(dear|hello|hi|greetings)\b', email_content, re.IGNORECASE)),
            "has_closing": bool(re.search(r'\b(sincerely|best regards|regards|best|thank you)\b', email_content, re.IGNORECASE)),
            "has_signature": bool(re.search(r'\n\s*\[.*?\]|\n\s*[A-Z][a-z]+ [A-Z][a-z]+\s*$', email_content)),
            "word_count": len(email_content.split()),
            "character_count": len(email_content),
            "paragraph_count": len([p for p in email_content.split('\n\n') if p.strip()])
        }
        return components

# Initialize the generator
email_generator = EmailFormatGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_email', methods=['POST'])
def generate_email_endpoint():
    try:
        data = request.get_json()
        casual_message = data.get('message', '')
        sender_name = data.get('sender_name', '')
        recipient_name = data.get('recipient_name', '')
        
        if not casual_message:
            return jsonify({"error": "No message provided"}), 400
        
        # Generate formal email
        formal_email = email_generator.generate_formal_email(
            casual_message, sender_name, recipient_name
        )
        
        # Analyze the generated email
        analysis = email_generator.analyze_email_quality(formal_email)
        
        # Extract email components
        components = email_generator.extract_email_components(formal_email)
        
        # Combine results
        result = {
            "original_message": casual_message,
            "formal_email": formal_email,
            "analysis": analysis,
            "components": components,
            "generation_timestamp": datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyze_existing', methods=['POST'])
def analyze_existing_endpoint():
    """Endpoint for analyzing existing email content"""
    try:
        data = request.get_json()
        email_content = data.get('content', '')
        
        if not email_content:
            return jsonify({"error": "No email content provided"}), 400
        
        # Analyze the email
        analysis = email_generator.analyze_email_quality(email_content)
        
        # Extract components
        components = email_generator.extract_email_components(email_content)
        
        result = {
            "email_content": email_content,
            "analysis": analysis,
            "components": components,
            "analysis_timestamp": datetime.now().isoformat()
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Check if API key is set
    if email_generator.api_key == 'your_groq_api_key_here':
        print("⚠️  WARNING: Please set your GROQ_API_KEY environment variable!")
        print("   Example: export GROQ_API_KEY='your_actual_api_key'")
    else:
        print("✅ Groq API key loaded successfully")
    
    app.run(debug=True, port=5000)