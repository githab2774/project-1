from secret import API
import requests

API_key = API #мой api ключ для запросов к серверу openweather
city = input("Введите название города:")
code_country = input("Для более точного результата введите код страны (Ru,Us,Fr)")

url_cord = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{code_country}&limit=1&appid={API_key}" #url для получения координат по названию города и коду страны/ из оффициальной документации OpenWeather

response_cord = requests.get(url_cord) #код для отправки запроса на данные к серверу при помощи метода requests.get
data = response_cord.json() # выходные результаты в виде json формата

lat = data[0]["lat"] 
lon = data[0]["lon"] #хранение широты и высоты города для следующего запроса

url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric&lang=ru" # url для получения сведений о погоде по координатам (широте и высоте)
response_weather = requests.get(url_weather) #получить данные с ресурса
data = response_weather.json() #конвертировать все в формат json ( ключ : значение)
print(f"Город: {data['name']}")
print(f"Температура: {data['main']['temp']} °C")
print(f"Ощущается как: {data['main']['feels_like']} °C")
print(f"Погода: {data['weather'][0]['description']}")
print(f"Влажность: {data['main']['humidity']} %")
print(f"Скорость ветра: {data['wind']['speed']} м/с") #вывод всех данных
