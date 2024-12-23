# aurora-forecast
A simple python app that sends Meshtastic Notifications when the Kp index is above a certain value. The script visits the NOAA website, and if the Kp index (a measure of solar activity) is equal to or above 7, I use the Meshtastic CLO to send a notification on the Mesh. This way, I can go see the northern lights when the solar activity is unusually high. You can find NOAA's 3-day aurora forecast here: https://services.swpc.noaa.gov/text/3-day-forecast.txt.

- To host this on PythonAnywhere as a scheduled task that runs in the morning and evening, the file get_forecast.py can be run by itself
- ~~To run continuously, with scheduled time(s) to send the email, the file run_daily.py can be run.~~

