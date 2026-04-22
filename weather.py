from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
load_dotenv

app = Flask(__name__)
Api = os.getenv('WEATHER_API_KEY') 
base_url = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    summary = []
    error = None

    if request.method == 'POST':
        cities = request.form.getlist('city')
        cities = [c.strip() for c in cities if c.strip()]

        if len(cities) == 1:
            # Single city
            params = {"q": cities[0], "appid": Api, "units": "metric"}
            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    "city": cities[0],
                    "temp": data['main']['temp'],
                    "desc": data['weather'][0]['description'],
                    "humidity": data['main']['humidity'],
                    "wind": data['wind']['speed']
                }
            else:
                error = f"City '{cities[0]}' not found!"

        else:
            # Multiple cities summary
            for city in sorted(cities):
                params = {"q": city, "appid": Api, "units": "metric"}
                response = requests.get(base_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    summary.append({
                        "city": city,
                        "temp": data['main']['temp'],
                        "desc": data['weather'][0]['description'],
                        "humidity": data['main']['humidity'],
                        "wind": data['wind']['speed']
                    })
                else:
                    error = f"City '{city}' not found! Please check the name."
                    summary = []
                    break

    return render_template('index.html', weather=weather_data, summary=summary, error=error)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)