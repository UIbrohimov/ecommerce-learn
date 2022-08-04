from django.shortcuts import render
from .models import About
    
def about_view(request):
    ctx = About.objects.last()
    context = {'ctx': ctx}
    return render(request, 'company/about.html', context)
