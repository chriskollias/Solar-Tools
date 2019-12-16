from django.shortcuts import render
from django.http import HttpResponse
from .forms import LatLongForm
from solar_api import NREL_API

# Create your views here.
def index(request):
    form = LatLongForm()
    if request.method == 'POST':
        form = LatLongForm(request.POST)
        print(form)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            year = form.cleaned_data['year']

            attributes = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'

            #print(f'{latitude},{longitude} in {year}')

            nrel_api = NREL_API()
            graph_image = nrel_api.get_monthly_averages(latitude, longitude, year, attributes)
            print(graph_image)

    return render(request, 'tools/base.html', {'form': form})

