from django.urls import reverse
from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import CreateView

from .models import Contact, Message
# Create your views here.


def contact_view(request):
    ctx = Contact.objects.all()
    form = ContactForm()
    context = {'form': form, "ctx": ctx}

    if request.method == "POST":
    
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ContactForm(data=request.POST)
            context["form"] = form
            context["errors"] = form.errors
    return render(request, 'contact/contact.html', context)


class MessageCreate(CreateView):
    model = Message
    fields = ['name', 'phone', 'message']
    template_name: str = 'contact/contact.html'

    def get_success_url(self) -> str:
        return reverse('contact:cont')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ctx'] = Contact.objects.last()
        return context

message_view = MessageCreate.as_view()