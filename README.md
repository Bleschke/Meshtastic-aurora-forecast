# aurora-forecast
A simple python app that sends you emails when the Kp index is above a certain value. I host this on PythonAnywhere as a scheduled task that runs once a morning. The script visits the NOAA website, and if the Kp index (a measure of solar activity) is equal to or above 5, I use the SendGrid API to send myself an email. This way, I can go see the northern lights when the solar activity is unusually high. You can find NOAA's 3-day aurora forecast here: https://services.swpc.noaa.gov/text/3-day-forecast.txt

Some of this solar activity stuff moves in decade-long-ish cycles. In 2023, we're approaching a peak in solar activity. Here's a little chart showing some historical Kp index readings:

![image](https://github.com/pete-rodrigue/aurora-forecast/assets/8962291/01a1c7a8-ccbb-4f7b-8cae-94578153684a)

