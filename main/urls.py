from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("form", views.form, name="form"),
    path("Like", views.Like, name="Like"),
  

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
