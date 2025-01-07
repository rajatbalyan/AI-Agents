from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle
from typing import List, Dict
import base64

class GmailClient:
    SCOPES = ['https://www.googleapis.com/auth/gmail.modify']
    
    def __init__(self):
        self.creds = None
        self.service = None
        self.authenticate()
    
    def authenticate(self):
        """Handles Gmail OAuth2 authentication."""
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    os.getenv('GMAIL_CREDENTIALS_FILE'), self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        
        self.service = build('gmail', 'v1', credentials=self.creds)
    
    def get_unread_emails(self, max_results: int = 10) -> List[Dict]:
        """Fetches unread emails from Gmail inbox."""
        try:
            results = self.service.users().messages().list(
                userId='me',
                labelIds=['INBOX', 'UNREAD'],
                maxResults=max_results
            ).execute()
            
            messages = results.get('messages', [])
            emails = []
            
            for message in messages:
                email = self.service.users().messages().get(
                    userId='me',
                    id=message['id'],
                    format='full'
                ).execute()
                emails.append(email)
            
            return emails
        except Exception as e:
            print(f"Error fetching emails: {e}")
            return [] 