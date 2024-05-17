from smtplib import SMTP, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SmtpMail:
    def __init__(self, host, port, password, sender, sender_name):
        self.smtp_ip = host
        self.smtp_port = port
        self.smtp_email = sender
        self.smtp_pw = password
        self.smtp_name = sender_name

    def send_msg(self, recipient, subject, body):
        try:
            mail_server = SMTP(self.smtp_ip, self.smtp_port)
            mail_server.login(self.smtp_email, self.smtp_pw)
            message_from = u"{} <{}>".format(self.smtp_name, self.smtp_email)
            msg = MIMEMultipart("alternative")
            msg['From'] = message_from
            msg['To'] = recipient
            msg['Subject'] = subject
            message_text = body
            msg.attach(MIMEText(message_text))
            mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
            mail_server.quit()
        except SMTPException:
            print("failed to send mail!!!")
