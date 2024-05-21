from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Content, Email, Mail, To


class SendgridMail:
    def __init__(self, sendgrid_api_key, sendgrid_sender):
        self.sender = sendgrid_sender
        self.sendgrid_api_k = sendgrid_api_key

    def send_msg(self, recipient, subject, body):
        sg = SendGridAPIClient(api_key=self.sendgrid_api_k)
        from_email = Email(self.sender)  # Change to your verified sender
        to_email = To(recipient)  # Change to your recipient
        content = Content("text/plain", body)
        mail = Mail(from_email, to_email, subject, content)
        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()
        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)
        #print(response.status_code)
        #print(response.headers)