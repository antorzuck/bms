from django.shortcuts import render, get_object_or_404
from base.models import *


def subcategory_detail(request, id):
    subcategory = get_object_or_404(Subcategory, id=id)
    return render(request, 'content.html', {'text': subcategory.text})


def all_img(r):
    gal = Gellery.objects.all().order_by('-id')
    return render(r, 'content.html', {'gal': gal, 'have_img': True})

    
from django.core.paginator import Paginator

def all_vid(request):
    videos = Videos.objects.all().order_by('-id')

    paginator = Paginator(videos, 9)  # 9 videos per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'content.html', {
        'vid': page_obj,
        'have_vid': page_obj.object_list.exists(),
    })

    


def home(r):

    notice = Notice.objects.all().order_by('-id')

    categories = Category.objects.prefetch_related('subcategories').all().order_by('id')


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

def get_widget(r, id):
   pori = Widget.objects.get(id=id)
   context = {
    'text' : pori.text
    }
   return render(r, 'content.html', context)


def get_maddhomik(r, id):
   pori = MaddhomikTeacher.objects.get(id=id)
   context = {
    'text' : pori.text
    }
   return render(r, 'content.html', context)
