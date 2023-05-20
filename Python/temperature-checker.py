import tkinter as tk
import requests
from geopy.geocoders import Nominatim

API_KEY = '4b48ad63ee0fdff12ea6b45053028c2a'


def get_weather(latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric'

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            weather_info = f'Temperature: {temperature}°C\nDescription: {description}\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s'
            weather_label.config(text=weather_info)
        else:
            weather_label.config(text='Error: Invalid response from API.')
    except (requests.exceptions.RequestException, KeyError):
        weather_label.config(text='Error: Failed to retrieve weather data.')


def on_submit():
    city = city_entry.get()

    if city:
        geolocator = Nominatim(user_agent='weather-app')
        location = geolocator.geocode(city)

        if location:
            latitude = location.latitude
            longitude = location.longitude

            get_weather(latitude, longitude)
        else:
            weather_label.config(text='Error: Invalid city name.')
    else:
        weather_label.config(text='Error: Please enter a city name.')


window = tk.Tk()
window.title('Weather App')

city_label = tk.Label(window, text='Enter a city name:')
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

submit_button = tk.Button(window, text='Submit', command=on_submit)
submit_button.pack()

weather_label = tk.Label(window)
weather_label.pack()

window.mainloop()
