from typing import Dict
import base64
from email.mime.text import MIMEText

class DraftManager:
    def __init__(self, gmail_service):
        self.service = gmail_service
    
    def create_draft(self, email_data: Dict, reply_text: str) -> bool:
        """Creates a draft reply in Gmail."""
        try:
            message = MIMEText(reply_text)
            message['to'] = email_data['sender']
            message['subject'] = f"Re: {email_data['subject']}"
            
            encoded_message = base64.urlsafe_b64encode(
                message.as_bytes()
            ).decode('utf-8')
            
            draft = self.service.users().drafts().create(
                userId='me',
                body={
                    'message': {
                        'raw': encoded_message,
                        'threadId': email_data['thread_id']
                    }
                }
            ).execute()
            
            return True
        except Exception as e:
            print(f"Error creating draft: {e}")
            return False 