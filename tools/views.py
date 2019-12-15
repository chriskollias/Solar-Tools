from django.shortcuts import render
from django.http import HttpResponse
from .forms import LatLongForm

# Create your views here.
def index(request):
    form = LatLongForm()
    year = 2010 #default
    if request.method == 'POST':
        form = LatLongForm(request.POST)
        print(form)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            #year = form.cleaned_data['year']

        print(f'{latitude},{longitude} in {year}')

    return render(request, 'tools/base.html', {'form': form})

