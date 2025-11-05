from django.shortcuts import render, get_object_or_404
from base.models import *


def subcategory_detail(request, id):
    subcategory = get_object_or_404(Subcategory, id=id)
    return render(request, 'content.html', {'text': subcategory.text})


def home(r):

    notice = Notice.objects.all().order_by('-id')

    categories = Category.objects.prefetch_related('subcategories').all()


    context = {

        'notice' : notice,
        'categories': categories

    }

    return render(r, 'home.html', context)

def get_pori(r):
   pori = Porichalok.objects.filter().first()
   context = {
    'text' : pori.text
    }
   return render(r, 'content.html', context)

def get_head(r):
   pori = HeadTeacher.objects.filter().first()
   context = {
    'text' : pori.text
    }
   return render(r, 'content.html', context)


def notice_detail(request, id):
    notice = get_object_or_404(Notice, id=id)
    return render(request, 'content.html', {'text': notice.text})