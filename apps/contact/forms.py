from django.forms import ModelForm
from .models import Message


class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
