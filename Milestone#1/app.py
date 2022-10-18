import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    location = request.form['Location']
    if location.isnumeric():
        api_data = get_api_zipcode(location)
        lat, lon = api_data["lat"], api_data["lon"]
    else:
        api_data = get_api_city(location)
        lat, lon = api_data[0]["lat"], api_data[0]["lon"]
    forecast = get_temperature(lat,lon)
    temps = []
    dates = []
    for i in range(0,40,8):
        date = forecast["list"][i]["dt_txt"]
        temp = forecast["list"][i]["main"]["temp"]
        temp_f = "{0:.2f}".format((temp-273.15)*(9/5)+32)
        temp_c = "{0:.2f}".format(temp-273.15)
        temps.append(temp_f)
        temps.append(temp_c)
        dates.append(date)

    return render_template('results.html', date_1=dates[0], date_2=dates[1], date_3=dates[2], date_4=dates[3], date_5=dates[4],
     temp_1f=temps[0], temp_1c=temps[1], temp_2f=temps[2], temp_2c=temps[3], temp_3f=temps[4],temp_3c=temps[5],temp_4f=temps[6],
     temp_4c=temps[7],temp_5f=temps[8],temp_5c=temps[9])

def get_api_zipcode(zip_code):
    url = "http://api.openweathermap.org/" \
              "geo/1.0/zip?zip={}&appid=53d9a1ecd2f18487b98ef685ba69b07d".format(zip_code)
    req = requests.get(url)
    return req.json()

def get_api_city(city):
    url = "http://api.openweathermap.org/" \
              "geo/1.0/direct?q={}&limit=5&appid=53d9a1ecd2f18487b98ef685ba69b07d".format(city)
    req = requests.get(url)
    return req.json()

def get_temperature(lat, lon):
    api_url = "http://api.openweathermap.org/" \
              "data/2.5/forecast?lat={}&lon={}&appid=53d9a1ecd2f18487b98ef685ba69b07d".format(lat, lon)
    req = requests.get(api_url)
    return req.json()

if __name__ == '__main__':
    app.run()