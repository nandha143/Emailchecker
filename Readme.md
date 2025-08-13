# 🚀 Smart Email Generator & Formatter

An AI-powered web application that converts casual messages into professional emails and analyzes email quality using the Groq API with LLaMA 3 model.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)
![Groq API](https://img.shields.io/badge/Groq-API-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 📝 Email Generation Mode
- **Casual to Formal Conversion**: Transform messages like "i am having a fever i am planning to leave" into professional emails
- **Smart Context Understanding**: AI recognizes different types of requests (sick leave, meetings, etc.)
- **Professional Formatting**: Automatic subject lines, greetings, closings, and signatures
- **Customizable Details**: Add sender and recipient names for personalized emails

### 🔍 Email Analysis Mode
- **Quality Assessment**: Overall rating and scoring system (1-10)
- **Tone Analysis**: Professional, Semi-professional, or Casual classification
- **Component Checking**: Validates subject line, greeting, closing, and signature
- **Grammar & Spelling**: AI-powered error detection
- **Improvement Suggestions**: Actionable recommendations for better emails
- **Statistics**: Word count, character count, and paragraph analysis

### 🎨 User Interface
- **Modern Design**: Beautiful gradient themes with glassmorphism effects
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Interactive Elements**: Smooth animations, hover effects, and loading states
- **Dual Mode Interface**: Easy switching between generation and analysis modes
- **One-Click Copy**: Copy generated emails to clipboard instantly

## 📋 Requirements

- Python 3.8 or higher
- Groq API key (free tier available)
- Modern web browser

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smart-email-generator.git
cd smart-email-generator
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv email_env

# Activate virtual environment
# On Windows:
email_env\Scripts\activate
# On macOS/Linux:
source email_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

**Option A: Using .env file (Recommended)**
```bash
# Create .env file in project root
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
echo "FLASK_ENV=development" >> .env
echo "FLASK_DEBUG=True" >> .env
```

**Option B: Export directly**
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

### 5. Get Your Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Generate a new API key
5. Copy the key to your `.env` file

## 🚀 Usage

### Start the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Email Generation Mode
1. Select **"Generate Email"** mode
2. Enter your casual message (e.g., "i am having a fever i am planning to leave")
3. Optionally add your name and recipient name
4. Click **"Generate Professional Email"**
5. Review the generated formal email
6. Copy to clipboard and use!

### Email Analysis Mode
1. Select **"Analyze Email"** mode
2. Paste your existing email content
3. Click **"Analyze Email Quality"**
4. Review the comprehensive analysis including:
   - Overall quality rating
   - Tone assessment
   - Component validation
   - Suggestions for improvement
   - Grammar and spelling feedback

## 📁 Project Structure

```
smart-email-generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore file
└── templates/           # HTML templates (if using Flask templates)
    └── index.html       # Main interface
```

## 🔧 API Endpoints

### POST `/generate_email`
Generate professional email from casual message.

**Request Body:**
```json
{
  "message": "i am having a fever i am planning to leave",
  "sender_name": "John Doe",
  "recipient_name": "Manager"
}
```

**Response:**
```json
{
  "original_message": "i am having a fever i am planning to leave",
  "formal_email": "Subject: Sick Leave Request...",
  "analysis": {
    "overall_rating": "9",
    "tone_assessment": "Professional",
    "strengths": [...],
    "improvements": [...]
  },
  "components": {
    "has_subject": true,
    "has_greeting": true,
    "word_count": 87
  }
}
```

### POST `/analyze_existing`
Analyze existing email content for quality and format.

**Request Body:**
```json
{
  "content": "Subject: Meeting Request\n\nDear John,\n\nI would like to schedule a meeting..."
}
```

## 💡 Example Transformations

### Input (Casual)
```
"i am having a fever i am planning to leave"
```

### Output (Professional)
```
Subject: Sick Leave Request - December 13, 2024

Dear Manager,

I hope this email finds you well. I am writing to inform you that I am currently experiencing flu-like symptoms, including a fever, which makes it necessary for me to take sick leave today.

I understand the importance of my responsibilities and will ensure that any urgent matters are addressed remotely if possible. I will monitor my health condition and keep you updated on my expected return date.

Please let me know if there are any immediate priorities that need attention during my absence.

Thank you for your understanding.

Best regards,
[Your Name]
[Your Position]
[Your Contact Information]
```

## 🔒 Security Features

- **Environment Variables**: API keys stored securely in environment variables
- **Input Validation**: Comprehensive validation of user inputs
- **Error Handling**: Graceful error handling with user-friendly messages
- **Rate Limiting**: Built-in protection against API abuse
- **CORS Protection**: Configured for secure cross-origin requests

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment (using Gunicorn)
```bash
# Install gunicorn (included in requirements.txt)
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment Variables for Production
```bash
export GROQ_API_KEY="your_production_api_key"
export FLASK_ENV="production"
export FLASK_DEBUG="False"
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

**1. "API Error: 401 Unauthorized"**
- Check if your Groq API key is correctly set in the environment variables
- Verify the API key is valid and not expired

**2. "Module not found" errors**
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

**3. "Connection Error"**
- Check your internet connection
- Verify Groq API service status

**4. Frontend not loading**
- Ensure Flask app is running on port 5000
- Check browser console for JavaScript errors

### Debug Mode
Enable debug mode for detailed error messages:
```bash
export FLASK_DEBUG=True
python app.py
```

## 📈 Performance

- **Response Time**: Typically 2-4 seconds for email generation
- **Concurrent Users**: Supports multiple simultaneous users
- **API Limits**: Respects Groq API rate limits
- **Memory Usage**: Lightweight Flask application (~50MB RAM)

## 🔮 Future Enhancements

- [ ] Multiple language support
- [ ] Email templates library
- [ ] Batch processing for multiple emails
- [ ] Integration with email clients
- [ ] Advanced grammar checking
- [ ] Sentiment analysis
- [ ] Email scheduling features
- [ ] Team collaboration tools

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for providing the fast LLaMA API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [LLaMA](https://ai.meta.com/llama/) by Meta for the language model

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#🐛-troubleshooting) section
2. Search existing [Issues](https://github.com/yourusername/smart-email-generator/issues)
3. Create a new issue with detailed description
4. Contact support at: your-email@domain.com

## 🌟 Show Your Support

If this project helped you, please give it a ⭐ star on GitHub!

---

**Made with ❤️ and AI** | **Powered by Groq & LLaMA 3**