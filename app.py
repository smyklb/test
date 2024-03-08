import datetime
import requests
from flask import Flask, render_template, request
from datetime import datetime
from matplotlib import pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    x_time = [0, 1, 2, 3, 4, 5, 6]
    y_temp = [18, 15, 13, 9, 8, 8, 11]
    plt.plot(x_time, y_temp)
    plt.savefig("test_chart")

    return render_template('home.html')


@app.route('/results', methods=("GET", "POST"))
def results():
    api_key = "03813016975d1bf4e5573449445caef7"
    city = request.form.get('city')
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&APPID=" + api_key
    print(url)
    response = requests.get(url).json()
    print(response)
    location = response.get("name")
    timezone = response.get("timezone")
    timestamp = response.get("dt")
    dt = datetime.fromtimestamp(timestamp)
    print(dt)
    timestamp_local = ""
    description = response.get("weather[0].description")
    temp_k = response.get("main").get("temp")
    temp_c = temp_k - 273.15
    wind_speed = response.get("wind").get("speed")
    icon = response.get("weather")[0].get("icon")
    my_list = [location, timezone, timestamp, timestamp_local, description, temp_k, temp_c, wind_speed, icon]
    my_dict = {
        "location": {"lat": 0, "long": 0},
        "timestamp": timestamp,
        "timezone": timezone,
        "dt": dt,
        "description": description,
        "temp_c": temp_c,
        "wind_speed": wind_speed,
        "icon": icon
    }
    print(my_dict)
    print(my_dict["timestamp"])
    print(my_dict["location"]["lat"])

    return render_template('results.html', weather_list=my_list, weather_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)
