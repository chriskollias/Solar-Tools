from django import forms

class LatLongForm(forms.Form):
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")
    year = forms.IntegerField(label="Year", min_value=1998, max_value=2014)
