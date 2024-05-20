import os
import logging
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

def send_approval_email(user_email):
    approval_function_url = os.getenv('APPROVAL_FUNCTION_URL')
    
    # Construct the email content
    email_body = f"New content ideas have been generated and are ready for your review.\n\nPlease review and approve the content ideas by clicking the link below:\n\n{approval_function_url}"
    email_subject = "New Content Ideas for Approval"
    
    # Use the verified sender email address from environment variables
    from_email = os.getenv('FROM_EMAIL')
    
    # Send the email (using SendGrid as an example)
    headers = {
        'Authorization': f"Bearer {os.getenv('SENDGRID_API_KEY')}",
        'Content-Type': 'application/json'
    }
    data = {
        "personalizations": [{"to": [{"email": user_email}]}],
        "from": {"email": from_email},
        "subject": email_subject,
        "content": [{"type": "text/plain", "value": email_body}]
    }
    response = requests.post("https://api.sendgrid.com/v3/mail/send", headers=headers, json=data)
    logging.info(f"Email sent response: {response.status_code} {response.text}")

# Set up test parameters
user_email = os.getenv('USER_EMAIL')

# Call the function to send the email
send_approval_email(user_email)
