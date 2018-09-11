
from django.urls import path,include
from . import views

urlpatterns = [

    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('setup',views.setup,name='setup'),
    path('myaccount',views.myaccount,name='myaccount'),

    path('paymentmethodsetup_page',views.paymentmethodsetup_page,name='paymentmethodsetup_page'),
    path('paymentmethodsetup',views.paymentmethodsetup,name='paymentmethodsetup'),
    path('cards/<int:pm_id>',views.paymentmethodmodify_page,name='paymentmethodmodify_page'),
    path('paymentmethodmodify',views.paymentmethodmodify,name='paymentmethodmodify'),

    path('location_setup_page',views.location_setup_page,name='location_setup_page'),
    path('location_setup',views.location_setup,name='location_setup'),
    path('locations/<int:location_id>',views.location_modify_page,name='location_modify_page'),
    path('location_modify',views.location_modify,name='location_modify'),

    path('transaction_type_setup_page',views.transaction_type_setup_page,name='transaction_type_setup_page'),
    path('transaction_type_setup',views.transaction_type_setup,name='transaction_type_setup'),
    path('transaction-type/<int:type_id>',views.transaction_type_modify_page,name='transaction_type_modify_page'),
    path('transaction_type_modify',views.transaction_type_modify,name='transaction_type_modify'),

    path('add_transaction',views.add_transaction,name='add_transaction'),
]
