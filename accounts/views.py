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
def signup(request):
    if request.method=='POST':
        #user wants to sign up
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error': 'username not available'})
            except User.DoesNotExist:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'password must match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'accounts/login.html')
def logout(request):
    #todo need to route to homepage
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def home(request):
    return render(request,'accounts/home.html')
def setup(request):
    payment_methods = PaymentMethod.objects
    locations = Location.objects
    types = TransactionType.objects
    return render(request,'accounts/setup.html',{'payment_methods':payment_methods,'locations':locations,"types":types})
def myaccount(request):
    return render(request,'accounts/myaccount.html')

@login_required
def paymentmethodsetup_page(request):
    return render(request,'accounts/card_setup.html')
@login_required
def paymentmethodsetup(request):
    logger = logging.getLogger(__name__)

    if request.method=='POST':
        logger.error(request.POST['description'])
        logger.error(request.POST['status'])
        logger.error(request.POST['credit_limit'])
        logger.error(request.user)
        logger.error(timezone.datetime.now())
        if request.POST['description'] and request.POST['credit_limit'] and request.POST['status']:
            try:
                payment_method = PaymentMethod()
                payment_method.method_name=request.POST['description']
                if request.POST['status'] == 'Active':
                    payment_method.status = 1
                else:
                    payment_method.status = 0
                logger.error("status pass")
                payment_method.credit_limit=request.POST['credit_limit']
                logger.error("credit limit pass")
                payment_method.account_id = request.user.id
                logger.error("account id pass")
                payment_method.create_date = timezone.now()
                logger.error("date time pass")
                payment_method.save()

                return redirect('setup')
            except:
                return render(request, 'setup.html', {'error': 'All field are required, please check your inputs.'})
        else:
            return render(request, 'accounts/signup.html', {'error': 'password must match'})
    else:
        return render(request, 'accounts/signup.html')

@login_required
def paymentmethodmodify_page(request,pm_id):
    record = get_object_or_404(PaymentMethod,pk=pm_id)
    return render(request, 'accounts/card_modify.html',{'payment_method':record})
@login_required
def paymentmethodmodify(request):
    logger = logging.getLogger(__name__)
    logger.error("it is in")
    if request.method == 'POST':
        logger.error("it is post")
        if request.POST['description'] and request.POST['credit_limit'] and request.POST['status']:
            logger.error(request.POST['id'])
            logger.error(request.POST['description'])
            logger.error(request.POST['credit_limit'])
            logger.error(request.POST['status'])
            try:

                payment_method = get_object_or_404(PaymentMethod,pk=request.POST['id'])
                if payment_method:
                    payment_method.method_name=request.POST['description']
                    if request.POST['status'] == 'Active':
                        payment_method.status = 1
                    else:
                        payment_method.status = 0

                    payment_method.credit_limit=request.POST['credit_limit']

                    payment_method.account_id = request.user.id

                    payment_method.create_date = timezone.now()

                    payment_method.save()
                    return redirect('setup')
            except:
                    return render(request, 'setup.html', {'error': 'error occurred while saving records'})

@login_required
def locationModify_page(request):
    pass
@login_required
def location_setup(request):
    logger = logging.getLogger(__name__)
    logger.error("location setup view function")
    if request.method == 'POST':
        logger.error(request.user.id)
        if request.POST['description'] and request.POST['status']:
            try:
                location = Location()
                location.name = request.POST['description']
                if request.POST['street']:
                    location.street = request.POST['street']
                    logger.error(request.POST['street'])
                else:
                    location.street = ''
                if request.POST['city']:
                    location.city = request.POST['city']
                    logger.error(request.POST['city'])
                else:
                    location.city = ''
                if request.POST['province']:
                    location.province = request.POST['province']
                    logger.error(request.POST['province'])
                else:
                    location.province = ''
                if request.POST['country']:
                    location.country = request.POST['country']
                    logger.error(request.POST['country'])
                else:
                    location.country = ''
                if request.POST['postal_code']:
                    location.postal_code = request.POST['postal_code']
                    logger.error(request.POST['postal_code'])
                else:
                    location.postal_code = ''
                if request.POST['status'] == 'Active':
                    logger.error(request.POST['status'])
                    location.status = 1
                else:
                    location.status = 0
                location.account_id = request.user.id
                location.save()
                return redirect('setup')
            except:
                return render(request, 'setup.html', {'error': 'Please check your inputs and try again.'})
@login_required
def location_setup_page(request):
    return render(request, 'accounts/location_setup.html')
@login_required
def location_modify_page(request,location_id):
    record = get_object_or_404(Location, pk=location_id)
    return render(request,'accounts/location-modify.html',{'location':record})
@login_required
def location_modify(request):
    if request.method == 'POST':
        try:
            if request.POST['description'] and request.POST['status']:
                location = get_object_or_404(Location,pk=request.POST['id'])
                location.name = request.POST['description']
                if request.POST['street']:
                    location.street = request.POST['street']
                    # logger.error(request.POST['street'])
                else:
                    location.street = ''
                if request.POST['city']:
                    location.city = request.POST['city']
                    # logger.error(request.POST['city'])
                else:
                    location.city = ''
                if request.POST['province']:
                    location.province = request.POST['province']
                    # logger.error(request.POST['province'])
                else:
                    location.province = ''
                if request.POST['country']:
                    location.country = request.POST['country']
                    # logger.error(request.POST['country'])
                else:
                    location.country = ''
                if request.POST['postal_code']:
                    location.postal_code = request.POST['postal_code']
                    # logger.error(request.POST['postal_code'])
                else:
                    location.postal_code = ''
                if request.POST['status'] == 'Active':
                    # logger.error(request.POST['status'])
                    location.status = 1
                else:
                    location.status = 0
                # location.account_id = request.user.id
                location.save()
                return redirect('setup')
            else:
                return render(request, 'setup.html', {'error': 'Please check your inputs and try again.'})
        except:
            return render(request, 'setup.html', {'error': 'Please check your inputs and try again.'})


@login_required
def transaction_type_setup_page(request):
    return render(request, 'accounts/type-setup.html')

@login_required
def transaction_type_setup(request):
    if request.method == 'POST':
        logger = logging.getLogger(__name__)
        logger.error(request.POST['income_indicator'])
        if request.POST['description'] and request.POST['income_indicator'] and request.POST['status']:
            type = TransactionType()
            type.name = request.POST['description']
            if request.POST['income_indicator'] == 'Income':
                type.income_ind = 2
            elif request.POST['income_indicator'] == 'Expense':
                type.income_ind = 1
            if request.POST['status'] == 'Active':
                type.status = 1
            else:
                type.status = 0
            type.account_id = request.user.id
            type.save()
            return redirect('setup')
        else:
            return render(request, 'setup.html', {'error': 'Please check your inputs and try again.'})

@login_required
def transaction_type_modify_page(request,type_id):
    record = get_object_or_404(TransactionType, pk=type_id)
    return render(request, 'accounts/transaction-type-modify.html', {'type': record})

@login_required
def transaction_type_modify(request):
    logger = logging.getLogger(__name__)
    if request.method == 'POST':
        logger.error("entered")
        try:

            logger.error(request.POST['income_indicator'])
            if request.POST['description'] and request.POST['income_indicator'] and request.POST['status']:

                type = get_object_or_404(TransactionType,pk=request.POST['id'])
                type.name = request.POST['description']
                logger.error(request.POST['description'])
                if request.POST['income_indicator'] == 'Income':
                    type.income_ind = 2
                elif request.POST['income_indicator'] == 'Expense':
                    type.income_ind = 1
                if request.POST['status'] == 'Active':
                    type.status = 1
                else:
                    type.status = 0
                type.save()
                return redirect('setup')
            else:
                return render(request, 'setup.html', {'error': 'Please check your inputs and try again.'})
        except:
            return render(request, 'setup.html', {'error': 'Please check your inputs and try again.'})