from datetime import datetime
from time import sleep
from urllib.error import URLError

import schedule

from get_forecast import get_forecast


def run_get_forecast():
    max_value = get_forecast(add_timestamp=True)
    print(f"ran script at {datetime.now()}, max value was {max_value}")


# run once after start, to check if it works
run_get_forecast()

# set at which time(s) the get_forecast script shall run (UTC)
schedule.every().day.at("04:00:00").do(run_get_forecast)
schedule.every().day.at("16:00:00").do(run_get_forecast)

while True:
    try:
        schedule.run_pending()
    except URLError as e:
        print(f"WARNING: catched URL error at {datetime.now()}. Exception: {e}")
    sleep(1)
