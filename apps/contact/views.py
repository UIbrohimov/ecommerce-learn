from django.shortcuts import render
from .forms import ContactForm

from .models import Contact

def contact_view(request):
    ctx = Contact.objects.all()
    form = ContactForm
    context = {'form': form, "ctx": ctx}
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            form = ContactForm(data=request.POST)
            context["form"] = form
    return render(request, 'contact/contact.html', context)


