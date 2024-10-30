from datetime import datetime

from noaa_parser import get_data
from sendgrid_mail import SendgridMail
from smtp_mail import SmtpMail

# Kp value threshold from when to send an email
KP_THRESHOLD = 5

# specify email here
recipient_emails = [
    'THE EMAIL OF THE PERSON WHO WILL GET THE EMAIL GOES HERE',
    # 'IF NEEDED, ADD MORE RECIPIENT ADDRESSES IN THIS LIST'
]
sender_email = 'YOUR SENDER EMAIL GOES HERE'
sender_name = 'YOUR NAME'
email_topic = "Aurora forecast"

# add the email send function (sendgrid or SMTP)
email_service = SendgridMail('INPUT YOUR SENDGRID API KEY HERE', sender_email)
# email_service = SmtpMail("SMTP HOST (ip/url)", "SMTP PORT", "SMTP PASSWORD", sender_email, sender_name)


def get_forecast(add_timestamp=False):
    # get the data from NOAA website
    df = get_data()
    # find the max Kp value over the next 3 days:
    max_value = df['value'].max()
    # If the forecast Kp index will be equal to or above threshold at any point in the next 3 days,
    # send an email alert using the service specified above:
    if max_value >= KP_THRESHOLD:
        email_content = ("\nAt " + str(df.iloc[0]['time']) + ' on ' + str(df.iloc[0]['variable']) +
                         ' the Kp index is forecast to be ' + str(df.iloc[0]['value']) + '!' +
                         '\n\n\nFor more details, visit:\n\n' +
                         'https://services.swpc.noaa.gov/text/3-day-forecast.txt')
        if add_timestamp:
            email_content = email_content + f'\n\nReport created on {str(datetime.now()).split(".")[0]}UT'
        for address in recipient_emails:
            email_service.send_msg(address, email_topic, email_content)
    return max_value


# if this script is run, run the forecast function
if __name__ == "__main__":
    get_forecast()
