import requests
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = "YOUR_API_KEY"
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'

# Twilio WhatsApp number and recipient number
twilio_whatsapp_number = "+14155238886"  # Twilio's official WhatsApp sandbox number
recipient_whatsapp_number = "+1234567890"  # Replace with your verified WhatsApp number

weather_params = {
    "lat": 19.751480,
    "lon": 75.713890,
    "appid": api_key,
    "cnt": 4,  # Number of forecast hours
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # Weather codes below 700 indicate rain/snow
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # Twilio WhatsApp number
        body="Rain's on the way! Don't forget to grab your umbrella! 🌧☔️",
        to='whatsapp:+1234567890'  # Your verified WhatsApp number
    )
    print(message.status)
