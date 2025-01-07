from typing import Dict
import base64
import email

class EmailParser:
    @staticmethod
    def parse_email(email_data: Dict) -> Dict:
        """Parses raw email data into structured format."""
        headers = email_data['payload']['headers']
        
        subject = next(
            (header['value'] for header in headers if header['name'].lower() == 'subject'),
            'No Subject'
        )
        
        sender = next(
            (header['value'] for header in headers if header['name'].lower() == 'from'),
            'Unknown Sender'
        )
        
        # Get email body
        if 'parts' in email_data['payload']:
            parts = email_data['payload']['parts']
            body = ''
            for part in parts:
                if part['mimeType'] == 'text/plain':
                    body = base64.urlsafe_b64decode(
                        part['body']['data']
                    ).decode('utf-8')
                    break
        else:
            body = base64.urlsafe_b64decode(
                email_data['payload']['body']['data']
            ).decode('utf-8')
        
        return {
            'id': email_data['id'],
            'subject': subject,
            'sender': sender,
            'body': body,
            'thread_id': email_data['threadId']
        } 