from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from paymentmethod.models import PaymentMethod
import logging
from transactiontype.models import TransactionType
from location.models import Location
from transactions.models import Transaction

def home_data_load(user_id,error_ind=None):
    payment_methods = PaymentMethod.objects.filter(account=user_id, status=1)
    locations = Location.objects.filter(account=user_id, status=1)
    types = TransactionType.objects.filter(account=user_id, status=1)
    transactions = Transaction.objects.filter(account=user_id).select_related()
    if error_ind is not None:
        error = "error occurred while saving records"
        return {'payment_methods':payment_methods,'locations':locations,"types":types,'transactions':transactions,'error':error}
    else:
        return {'payment_methods': payment_methods, 'locations': locations, "types": types,'transactions': transactions}

def setup_data_load(user_id,error_ind=None):
    payment_methods = PaymentMethod.objects.filter(account=user_id)
    locations = Location.objects.filter(account=user_id)
    types = TransactionType.objects.filter(account=user_id)
    if error_ind is not None:
        error = "error occurred while saving records"
        return {'payment_methods':payment_methods,'locations':locations,"types":types,'error':error}
    else:
        return {'payment_methods': payment_methods, 'locations': locations, "types": types}