from django.http import HttpResponse
from django.shortcuts import render
from .models import details, persons


# Create your views here.
def demo(request):
     obj=details.objects.all()
     objs=persons.objects.all()
     return render(request,"index.html",{'value': obj,'values': objs})
