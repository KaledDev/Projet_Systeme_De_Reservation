from django import forms
from .models import Restaurant, Hotel, Event

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
