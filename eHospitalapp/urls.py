
from django.contrib import admin
from django.urls import path
from eHospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),

    path('starter/', views.starter, name='starter'),

    path('appointment/', views.appointment, name='appointment'),

    path('show/', views.show, name='show'),

    path('about/', views.about, name='about'),

    path('', views.register, name='register'),

    path('login/', views.login_user, name='login'),

    path('delete/<int:id>/', views.delete),

    path('edit/<int:id>/', views.edit),


    #Mpesa urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),


]
