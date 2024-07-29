from django.shortcuts import render
from apps.base.models import *

# Create your views here.
def index(request):
    service = Our_service.objects.all()
    base = Base.objects.all()
    prises = Our_prices.objects.all()
    gallery = Our_gallery.objects.all()
    animals = Animals.objects.all()
    contact = Contact.objects.all()

    return render(request, 'index.html', locals())