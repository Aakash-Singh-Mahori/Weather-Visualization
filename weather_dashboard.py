import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = '076fedc58592ce90fed0db9e3b6988e1'
CITY = str(input('Enter City : '))

def fetch_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

def plot_forecast(data):
    temps = [entry['main']['temp'] for entry in data['list']]
    times = [datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S') for entry in data['list']]

    plt.figure(figsize=(12, 6))
    sns.lineplot(x=times, y=temps, marker="o", color="orange")
    plt.title(f'Temperature Forecast for {CITY}')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    weather_data = fetch_weather(CITY)
    if weather_data:
        plot_forecast(weather_data)
