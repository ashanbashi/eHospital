
from django.contrib import admin
from django.urls import path,include

from sokoapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),

    path('contact/', views.contact, name='contact'),

    path('about/', views.about, name='about'),

    path('services/', views.services, name='services'),

]
