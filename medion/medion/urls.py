from django.contrib import admin
from django.urls import path
from medion.views import indexFuncion, indexFuncion2, page2, page3, page4, page5, page6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',indexFuncion),
    path('pag2/',page2),
    path('pag3/',page3),
    path('index/login',page4),
    path('index/nosotros',page5),
    path('index/contactanos',page6),
    path('index/index.html',indexFuncion2),
]
 