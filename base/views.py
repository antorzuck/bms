from django.shortcuts import render
from base.models import *



def home(r):
    banner = Banner.objects.all()
    porichalok = Porichalok.objects.filter().first()
   
    return render(r, 'home.html', context={'b':banner,
'p' : porichalok
})

def get_pori(r):
   pori = Porichalok.objects.filter().first()
   context = {
    'text' : pori.text
    }
   return render(r, 'content.html', context)
