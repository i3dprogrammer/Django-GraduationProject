from django.forms import ModelForm
from django import forms
from .models import Event

class AddEventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'image','info','location', 'date']
		widgets = {
			'info' : forms.Textarea()
		}