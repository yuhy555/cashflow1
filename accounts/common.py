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
import json
def home_data_load(user_id,error_ind=None):
    payment_methods = PaymentMethod.objects.filter(account=user_id, status=1)
    locations = Location.objects.filter(account=user_id, status=1)
    types = TransactionType.objects.filter(account=user_id, status=1)
    transactions = Transaction.objects.filter(account=user_id).select_related().order_by('-tran_date')
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
def create_default_payment_method(user_id):
    payment_method = PaymentMethod()
    payment_method.method_name = 'TD VISA ****1234'
    payment_method.credit_limit = 1000
    payment_method.account_id = user_id
    payment_method.status   =1
    payment_method.create_date = timezone.now()
    payment_method.save()
def create_default_location(user_id):
    location = Location()
    location.name = 'SaveonFood'
    location.status = 1
    location.account_id = user_id
    location.save()
def create_default_type(user_id):
    type = TransactionType()
    type.name = 'Grocery'
    type.income_ind = 1
    type.status = 1
    type.account_id = user_id
    type.save()
def create_default_entries(user_id):
    create_default_payment_method(user_id)
    create_default_location(user_id)
    create_default_type(user_id)

def transaction_modify_load(user_id,tran_id):
    record = get_object_or_404(Transaction, pk=tran_id)
    setup = setup_data_load(user_id)
    setup["transaction"] = record
    return setup
def date_get_year(date):
    return date.strftime('%Y')
def date_get_month(date):
    return date.strftime('%m')
def date_get_day(date):
    return date.strftime('%d')


def transform_transctions(transactions):
    result=[]
    for transaction in transactions:
        year = date_get_year(transaction.tran_date)
        month = date_get_month(transaction.tran_date)
        day = date_get_day(transaction.tran_date)
        result.append({"year":year,"month":month,"day":day,"amount":transaction.tran_amount})
    return json.dumps(result)


