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

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sjalaleddine2/WeatherForecaster.git
cd WeatherForecaster
```

### 2️⃣ Set Up a Virtual Environment (Optional)

It’s recommended to use a virtual environment to manage dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'
```

### 3️⃣ Install Dependencies

If `requirements.txt` is available, install dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, manually install required packages (e.g., `requests`):

```bash
pip install requests
```

### 4️⃣ Obtain an API Key

- Sign up at [OpenWeatherMap](https://openweathermap.org/api) to get a free API key.
- Create a `.env` file in the project root and add:
  ```ini
  API_KEY=your_openweathermap_api_key
  ```

### 5️⃣ Run the Application

```bash
python main.py
```

Then, open your browser and go to:

```
http://127.0.0.1:5000/
```

## Usage

- Enter a city name to fetch its weather data.
- View details such as temperature, humidity, wind speed, and general conditions.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Describe your change"
   ```
4. Push to GitHub:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.
