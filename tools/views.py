from django.shortcuts import render
from django.http import HttpResponse
from .forms import LatLongForm

# Create your views here.
def index(request):

    if(request.method == 'POST'):
        form = LatLongForm(request.POST)
        print(form)

        latitude = form.get('latitude')
        longitude = form.get('longitude')
        year = form.get('year')

        print(f'{latitude},{longitude} in {year}')

    context = {'facts': 'not real'}
    return render(request, 'tools/base.html', context)

