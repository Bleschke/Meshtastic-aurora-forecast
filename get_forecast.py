from smtp_mail import SmtpMail
from sendgrid_mail import SendgridMail
from noaa_parser import get_data


# Kp value threshold from when to send an email
KP_THRESHOLD = 5  # noqa

# specify email here
recipient_emails = [
    'THE EMAIL OF THE PERSON WHO WILL GET THE EMAIL GOES HERE',
    # 'IF NEEDED, ADD MORE RECIPIENT ADDRESSES IN THIS LIST'
]
sender_email = 'YOUR SENDER EMAIL GOES HERE'
sender_name = 'YOUR NAME'
email_topic = "Aurora forecast"

# add the email send functions (sendgrid and/or SMTP)
email_services = [
    SmtpMail("SMTP HOST GOES HERE (ip/url)", "SMTP PORT GOES HERE", "SMTP PASSWORD GOES HERE", sender_email, sender_name),
    SendgridMail('INPUT YOUR SENDGRID API KEY HERE', sender_email)
]


def get_forecast(add_timestamp=False):
    # get the data from NOAA website
    df = get_data()
    # find the max Kp value over the next 3 days:
    max_value = df['value'].max()
    # If the forecast Kp index will be equal to or above threshold at any point in the next 3 days,
    # send an email alert using the service(s) specified above:
    if max_value >= KP_THRESHOLD:
        email_content = ("\nAt " + str(df.iloc[0]['time']) + ' on ' + str(df.iloc[0]['variable']) +
                         ' the Kp index is forecast to be ' + str(df.iloc[0]['value']) + '!' +
                         '\n\n\nFor more details, visit:\n\n' +
                         'https://services.swpc.noaa.gov/text/3-day-forecast.txt')
        if add_timestamp:
            email_content = email_content + f'\n\nReport created on {str(datetime.now()).split('.')[0]}UT'
        for endpoint in email_services:
            for address in recipient_emails:
                endpoint.send_msg(address, email_topic, email_content)
    return max_value


if __name__ == "__main__":
    get_forecast()
