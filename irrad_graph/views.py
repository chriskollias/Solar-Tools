from django.shortcuts import render
from .forms import LatLongForm
from .models import IrradGraphInputs
import sys
import matplotlib.pyplot as plt

sys.path.append('../')
#from .. import API.solar_api.NREL_API as NREL_API
from API.solar_api import NREL_API

# Create your views here.
def main_view(request, *args, **kwargs):

    form = LatLongForm()

    if request.method == 'POST':
        form = LatLongForm(request.POST)

        if form.is_valid():
            IrradGraphInputs.objects.create(**form.cleaned_data)
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            year = form.cleaned_data['year']
            attrs = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'
            print(f'lat:{latitude} long:{longitude} year:{year} attrs:{attrs}')

            api = NREL_API()
            graph_image = api.get_monthly_averages(latitude, longitude, year, attrs)

            print('graph image is {}'.format(graph_image))

            form = LatLongForm()
        else:
            print(form.errors)

    context = {
        'hello': 'Hello Solar!',
        'form': form,
    }
    return render(request, 'irrad_graph/irrad_graph_page.html', context)