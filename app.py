from groq import Groq
import json
import re
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class EmailFormatChecker:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
    
    def check_email_format(self, email_content):
        """
        Check email format and provide suggestions using Groq API
        """
        emotion_prompt = f"""
        Analyze the following email content and provide feedback on its format, tone, and professionalism.
        
        Email Content:
        {email_content}
        
        Please provide:
        1. Overall format rating (1-10)
        2. Tone assessment (Professional/Casual/Inappropriate)
        3. Key suggestions for improvement
        4. Grammar and spelling issues
        5. Structure recommendations
        
        Respond in JSON format with keys: rating, tone, suggestions, grammar_issues, structure_tips
        """
        
        try:
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": emotion_prompt}],
                model="llama3-8b-8192",
                temperature=0.3,
                max_tokens=500
            )
            
            # Extract the response content
            analysis = response.choices[0].message.content
            
            # Try to parse as JSON, if fails return structured response
            try:
                return json.loads(analysis)
            except:
                return {
                    "rating": "N/A",
                    "tone": "Unable to determine",
                    "suggestions": [analysis],
                    "grammar_issues": [],
                    "structure_tips": []
                }
                
        except Exception as e:
            return {
                "error": f"API Error: {str(e)}",
                "rating": 0,
                "tone": "Error",
                "suggestions": ["Please check your API key and try again"],
                "grammar_issues": [],
                "structure_tips": []
            }
    
    def basic_email_validation(self, email_content):
        """
        Perform basic email format validation
        """
        issues = []
        
        # Check for subject line
        if not re.search(r'subject:', email_content.lower()):
            issues.append("Missing subject line")
        
        # Check for greeting
        greetings = ['dear', 'hello', 'hi', 'greetings']
        if not any(greeting in email_content.lower() for greeting in greetings):
            issues.append("Missing proper greeting")
        
        # Check for closing
        closings = ['sincerely', 'best regards', 'thank you', 'regards', 'best']
        if not any(closing in email_content.lower() for closing in closings):
            issues.append("Missing professional closing")
        
        # Check email length
        if len(email_content.strip()) < 50:
            issues.append("Email content seems too short")
        
        return issues

# Initialize the checker (you'll need to provide your API key)
# checker = EmailFormatChecker("your_groq_api_key_here")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_email', methods=['POST'])
def check_email_endpoint():
    try:
        data = request.get_json()
        email_content = data.get('content', '')
        api_key = data.get('api_key', '')
        
        if not email_content:
            return jsonify({"error": "No email content provided"}), 400
        
        if not api_key:
            return jsonify({"error": "No API key provided"}), 400
        
        # Initialize checker with provided API key
        checker = EmailFormatChecker(api_key)
        
        # Get AI analysis
        ai_analysis = checker.check_email_format(email_content)
        
        # Get basic validation
        basic_issues = checker.basic_email_validation(email_content)
        
        # Combine results
        result = {
            "ai_analysis": ai_analysis,
            "basic_issues": basic_issues,
            "word_count": len(email_content.split()),
            "character_count": len(email_content)
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)