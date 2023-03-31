from django.forms import ModelForm
from .models import Song, Singer

class SingerForm(ModelForm):
    class Meta:
        model = Singer
        fields = '__all__'