from django.shortcuts import render
import requests
def main(request):
    appid = 'c1d03f20f1eebea2c7617750f5bfe198'
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    city = 'Minsk'
    res = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }
    context = {'info': 'city_info'}
    return render(request, 'weather/main.html', context)
