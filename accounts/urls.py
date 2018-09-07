
from django.urls import path,include
from . import views

urlpatterns = [

    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('setup',views.setup,name='setup'),
    path('myaccount',views.myaccount,name='myaccount'),
    path('paymentmethodsetup',views.paymentmethodsetup,name='paymentmethodsetup'),

]
