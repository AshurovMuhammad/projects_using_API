from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.
def weather(request):
    app_id = "ecf394f775014121a13130117231304"

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []
    for city in cities:
        url = f"http://api.weatherapi.com/v1/current.json?key={app_id}&q={city.name}&aqi=no"
        res = requests.get(url).json()

        try:
            city_info = {
                'city': city.name,
                'temp': res["current"]["temp_c"],
                'icon': res["current"]['condition']['icon']
            }
        except KeyError:
            city_info = {
                'city': "Bunday shaxar topilmadi",
                'temp': "-",
            }
        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }
    return render(request, template_name='weather/weather.html', context=context)
