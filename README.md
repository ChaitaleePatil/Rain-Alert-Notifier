# Rain-Alert-Notifier

This project is a Python script that fetches weather data from OpenWeatherMap and sends a WhatsApp notification via Twilio if rain is expected. It's perfect for ensuring you never forget your umbrella on a rainy day!

## Output
![demo](https://github.com/user-attachments/assets/adde80be-d759-4c84-8f9b-2496f3d8f40f)


## Features
- Retrieves weather forecast data from OpenWeatherMap.
- Checks if it will rain in the next few hours.
- Sends a WhatsApp message to notify you about the rain.

## Prerequisites
- Python 3.x
- Requests library (`pip install requests`)
- Twilio library (`pip install twilio`)
- An OpenWeatherMap API key
- Twilio account with a verified WhatsApp number

## How to Use
1. Clone this repository.
2. Replace `YOUR_API_KEY`, `YOUR_ACCOUNT_SID`, and `YOUR_AUTH_TOKEN` with your own credentials.
3. Replace `recipient_whatsapp_number` with your verified WhatsApp number.
4. Run the script using `python main.py`.

## Contributing
Feel free to open issues or submit pull requests if you'd like to contribute to this project.

## Contact
For any questions, feel free to reach out via GitHub.
