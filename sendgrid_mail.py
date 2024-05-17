from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content


def sendgrid_send(from_email_str, to_email_str, subject_str, content_str):
    sg = SendGridAPIClient(api_key='INPUT YOUR SENDGRID API KEY HERE')
    from_email = Email(from_email_str)  # Change to your verified sender
    to_email = To(to_email_str)  # Change to your recipient
    subject = subject_str
    content = Content("text/plain", content_str)
    mail = Mail(from_email, to_email, subject, content)
    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    #print(response.status_code)
    #print(response.headers)