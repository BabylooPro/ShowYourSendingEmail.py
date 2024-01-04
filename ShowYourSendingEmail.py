from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
import pickle
import os.path
import os

# DEFINE  SCOPE FOR GMAIL API ACCESS
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# FUNCTION TO GET GMAIL SERVICE OBJECT
def get_gmail_service():
    creds = None
    # CHECK IF TOKEN.PICKLE FILE EXISTS TO LOAD CREDENTIALS
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # IF CREDENTIALS ARE NOT VALID, REFRESH OR GET NEW CREDENTIALS
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:  # SAVE CREDENTIALS FOR NEXT RUN
            pickle.dump(creds, token)

    # BUILD AND RETURN GMAIL SERVICE OBJECT
    service = build('gmail', 'v1', credentials=creds)
    return service

# FUNCTION TO CHECK IF EMAILS HAVE BEEN SENT TO LIST OF EMAIL ADDRESSES
def check_emails(service, email_list):
    for email in email_list:
        # CREATE QUERY FOR EACH EMAIL & FETCH MESSAGES SENT TO EACH EMAIL ADDRESS
        query = f'to:{email}'
        results = service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        print(f"{email} - {'true' if messages else 'false'}")

# FUNCTION TO GET LIST OF EMAILS FROM USER INPUT OR FILE
def get_email_list():
    input_data = input("ENTER EMAILS OR FILE PATH: ")
    # CHECK IF INPUT IS A FILE AND PROCESS ACCORDINGLY
    if os.path.isfile(input_data):
        with open(input_data, 'r') as file:
            if input_data.endswith('.json'):
                data = json.load(file)
                return data["emails"]
            else:
                return file.read().splitlines()
    else:
        return [email.strip() for email in input_data.split(',')] # PROCESS INPUT AS A LIST OF EMAILS SEPARATED BY COMMAS


# MAIN EXECUTION
service = get_gmail_service()
email_list = get_email_list()
check_emails(service, email_list)
