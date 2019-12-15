from django import forms

class LatLongForm(forms.Form):
    latitude = forms.IntegerField(label="Latitude")
    longitude = forms.IntegerField(label="Longitude")

