import os
from datetime import datetime

from noaa_parser import get_data

# Kp value threshold from when to send an email
KP_THRESHOLD = 7

def get_forecast(add_timestamp=False):
    # get the data from NOAA website
    df = get_data()
    # find the max Kp value over the next 3 days:
    max_value = df['value'].max()
    # If the forecast Kp index will be equal to or above threshold at any point in the next 3 days,
    # send an email alert using the service specified above:
    if max_value >= KP_THRESHOLD:
        email_content = ("At " + str(df.iloc[0]['time']) + ' on ' + str(df.iloc[0]['variable']) +
                         ' the Kp index is forecast to be ' + str(df.iloc[0]['value']) + '!' +
                         '\n\n\nFor more details, visit:\n\n' +
                         'https://services.swpc.noaa.gov/text/3-day-forecast.txt')
        send_content = " ' " + email_content + " ' "
        print (send_content)
        os.system("/usr/local/bin/meshtastic --ch-index 3 --sendtext '🌟 AURORA NOTICE!'")
        os.system("/usr/local/bin/meshtastic --ch-index 3 --sendtext" + send_content)

    return max_value
    
# if this script is run, run the forecast function
if __name__ == "__main__":
    get_forecast()
