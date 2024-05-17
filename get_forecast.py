from sendgrid_mail import sendgrid_send
from noaa_parser import get_data

# specify email here
recipient_emails = [
    'THE EMAIL OF THE PERSON WHO WILL GET THE EMAIL GOES HERE',
    # 'IF NEEDED, ADD MORE RECIPIENT ADDRESSES IN THIS LIST'
]
sender_email = 'YOUR SENDER EMAIL GOES HERE'
email_topic = "Aurora forecast"

# assign the email send function (sendgrid or SMTP)
email_endpoints = [
    # smtp_send,
    sendgrid_send
]

# get the data from NOAA website
df = get_data()
# find the max Kp value over the next 3 days:
max_value = df['value'].max()
print(f"max_value={max_value}")

# If the forecast Kp index will be equal to or above 5 at any point in the next 3 days, send an email alert using the "SendGrid" service:
if max_value >= 5:
    email_content = ("\nAt " + str(df.iloc[0]['time']) + ' on ' + str(df.iloc[0]['variable']) +
                     ' the Kp index is forecast to be ' + str(df.iloc[0]['value']) + '!' +
                     '\n\n\nFor more details, visit:\n\n' + 'https://services.swpc.noaa.gov/text/3-day-forecast.txt')
    for endpoint in email_endpoints:
        for address in recipient_emails:
            endpoint(sender_email, address, email_topic, email_content)

