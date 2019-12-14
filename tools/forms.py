from django import forms

class LatLongForm(forms.Form):
    latitude = forms.IntegerField(help_text="Latitude")
    longitude = forms.IntegerField(help_text="Longitude")

