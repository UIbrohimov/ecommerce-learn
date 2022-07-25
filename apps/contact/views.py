from django.shortcuts import render
from .forms import ContactForm

from .models import Contact
# Create your views here.




def contact_view(request):
    ctx = Contact.objects.all()
    return render(request, 'contact/contact.html', {'ctx': ctx})



def contactView(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
