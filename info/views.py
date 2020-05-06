
import json
import requests
from django.shortcuts import render
from .	import views
from django.http import HttpResponse,JsonResponse
from .convert import Country,World


def bilgilendirme(request):
    return render(request, 'info/bilgilendirme.html')



def ulke(request):
    country = Country("Fransa")
    

    context = { "country" : country
                  
    }
    return render(request,'info/ulke.html' ,context)



def dunya(request):
    world = World()
    context = { "world" : world       
    }
    return render(request,'info/dunya.html' ,context)


