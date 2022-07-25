from django.forms import ModelForm
from .models import ContactView


class ContactForm(ModelForm):
    class Meta:
        model = ContactView
        fields = '__all__'
