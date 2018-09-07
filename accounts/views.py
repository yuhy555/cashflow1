from django.shortcuts import render,redirect
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
    return render(request,'accounts/setup.html',{'payment_methods':payment_methods})
def myaccount(request):
    return render(request,'accounts/myaccount.html')

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