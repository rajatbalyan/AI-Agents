# AI Email Assistant for DEEPAK TECH INDIA
## Water Treatment Solutions Customer Service

### Overview
This AI-powered email assistant automatically processes incoming emails, generates contextually appropriate responses, and creates draft replies for customer inquiries about water treatment solutions including STP, ETP, UF, and RO systems.

### Features
- 🔐 Secure Gmail API integration
- 📧 Automated email processing
- 🤖 AI-powered response generation using Google's Gemini
- 📝 Smart inquiry type detection
- 💧 Specialized for water treatment industry
- ✍️ Draft management in Gmail

### Prerequisites
- Python 3.8+
- Google Cloud Platform account
- Gmail API enabled
- Gemini API key

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd email-ai-agent
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```plaintext
GMAIL_CREDENTIALS_FILE=path/to/your/credentials.json
GEMINI_API_KEY=your_gemini_api_key
```

### Project Structure

email_ai_agent/
├── .env
├── requirements.txt
├── src/
│ ├── init.py
│ ├── gmail_client.py # Gmail API integration
│ ├── email_parser.py # Email parsing logic
│ ├── reply_generator.py # AI response generation
│ ├── draft_manager.py # Draft email management
│ └── utils.py # Utility functions
├── README.md
└── main.py # Main application entry
```

### Configuration

1. **Google Cloud Setup**:
   - Create a new project in Google Cloud Console
   - Enable Gmail API
   - Create OAuth 2.0 credentials
   - Download credentials JSON file
   - Update `.env` with file path

2. **Gemini API Setup**:
   - Get API key from Google AI Studio
   - Add to `.env` file

### Usage

Run the application:
```bash
python main.py
```

The script will:
1. Authenticate with Gmail
2. Fetch unread emails
3. Generate appropriate responses
4. Create draft replies in Gmail

### Response Categories
The system handles different types of inquiries:
- General Inquiries
- Product Inquiries
- Pricing Inquiries
- Technical Support
- Customer Service Requests

### Customization
You can customize the response templates and company information in `reply_generator.py`:
- Email templates
- Company details
- Product specifications
- Contact information

### Error Handling
The system includes comprehensive error handling for:
- API authentication
- Email processing
- Response generation
- Draft creation

### Security
- Uses OAuth 2.0 for secure Gmail access
- Stores sensitive credentials in environment variables
- Creates local token pickle file for session management

### Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

### Future Enhancements
- [ ] Sentiment analysis
- [ ] Priority detection
- [ ] Smart follow-up system
- [ ] Enhanced response customization
- [ ] Multilingual support
- [ ] Attachment handling
- [ ] CRM integration

### Troubleshooting
Common issues and solutions:
1. Authentication errors:
   - Verify credentials file path
   - Check OAuth 2.0 configuration
   - Ensure correct API permissions

2. Rate limiting:
   - Implement exponential backoff
   - Monitor API quotas

3. Response generation issues:
   - Check Gemini API key
   - Verify prompt formatting

### Acknowledgments
- Google Gmail API
- Google Gemini AI
- [Other libraries and tools used]