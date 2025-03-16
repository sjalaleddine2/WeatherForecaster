# WeatherForecaster

## Overview

WeatherForecaster is a simple weather application that provides real-time weather data using an external API. Users can search for a city and get up-to-date weather conditions, including temperature, humidity, and wind speed.

## Features

- **Live Weather Data** – Displays current temperature, humidity, wind speed, and general conditions.
- **City Search** – Look up weather for any city worldwide.
- **Simple & Responsive UI** – Optimized for different screen sizes.
- **Error Handling** – Handles incorrect city names and API issues gracefully.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **API Integration:** OpenWeatherMap API
- **Version Control:** Git & GitHub

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sjalaleddine2/WeatherForecaster.git
cd WeatherForecaster
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is missing, install manually: pip install requests)

3. Get an API Key
Sign up at OpenWeatherMap to get a free API key.
Create a .env file in the project root and add:
ini
Copy
Edit
API_KEY=your_openweathermap_api_key
4. Run the Application
bash
Copy
Edit
python main.py
Visit http://127.0.0.1:5000/ to use the app.

Usage
Enter a city name to fetch its weather data.
View details such as temperature, humidity, wind speed, and general conditions.
