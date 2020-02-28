from django.shortcuts import render
from .forms import LatLongForm
from .models import IrradGraphInputs
import matplotlib.pyplot as plt

from API.solar_api import NREL_API

MEDIA_PATH = 'media/irrad_graph/'

# Create your views here.
def main_view(request, *args, **kwargs):

    form = LatLongForm()

    if request.method == 'POST':
        form = LatLongForm(request.POST)
        print('CHECKPOINT A')
        if form.is_valid():
            print('CHECKPOINT B')
            IrradGraphInputs.objects.create(**form.cleaned_data)
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            year = form.cleaned_data['year']
            #attrs = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'
            attrs = 'ghi,dhi,dni'
            print(f'lat:{latitude} long:{longitude} year:{year} attrs:{attrs}')

            api = NREL_API()
            graph_image = api.get_monthly_averages(latitude, longitude, year, attrs)
            image_path = MEDIA_PATH + graph_image
            plt.savefig(image_path, dpi=300)
            print('CHECKPOINT C')

            form = LatLongForm()
        else:
            print(form.errors)

    context = {
        'hello': 'Hello Solar!',
        'form': form,
    }
    return render(request, 'irrad_graph/irrad_graph_page.html', context)