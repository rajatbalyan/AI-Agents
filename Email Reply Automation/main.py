import os
from dotenv import load_dotenv
from src.gmail_client import GmailClient
from src.email_parser import EmailParser
from src.reply_generator import ReplyGenerator
from src.draft_manager import DraftManager
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    load_dotenv()
    
    # Initialize components
    gmail_client = GmailClient()
    email_parser = EmailParser()
    reply_generator = ReplyGenerator()
    draft_manager = DraftManager(gmail_client.service)
    
    # Process unread emails
    unread_emails = gmail_client.get_unread_emails(max_results=5)
    logging.info(f"Found {len(unread_emails)} unread emails")
    
    for email_data in unread_emails:
        try:
            # Parse email
            parsed_email = email_parser.parse_email(email_data)
            logging.info(f"Processing email from: {parsed_email['sender']}")
            
            # Generate reply
            reply_text = reply_generator.generate_reply(parsed_email)
            if not reply_text:
                logging.error("Failed to generate reply")
                continue
            
            # Create draft
            success = draft_manager.create_draft(parsed_email, reply_text)
            if success:
                logging.info("Successfully created draft reply")
            else:
                logging.error("Failed to create draft")
                
        except Exception as e:
            logging.error(f"Error processing email: {e}")

if __name__ == "__main__":
    main() 