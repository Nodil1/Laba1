# app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/weather')
def get_weather():
    city = request.args.get('city', 'Moscow')  # Значение по умолчанию - Москва
    api_key = 'c43325a0ab15b999d371b74041531d5b'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    return jsonify({'city': city, 'weather': weather_description})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
