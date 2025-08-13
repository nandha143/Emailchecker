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
git clone https://github.com/nandha143/Emailchecker.git
cd Emailchecker
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


**Made with ❤️ and AI** | **Powered by Groq & LLaMA 3**
