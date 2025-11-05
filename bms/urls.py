
from django.contrib import admin
from django.urls import path, include
from base.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('porichalok', get_pori),
    path('head', get_head),
    path('subcategory/<int:id>/', subcategory_detail),
    path('notices/<int:id>/', notice_detail),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
