
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


@csrf_exempt
# Create your views here.
def register(request):
    
    if request.method=='POST':
        username= request.POST['username']
        email1 = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                #print('username is  taken')
                messages.info(request,'username est déjà pris,veuillez changer')
                #return redirect('/')
                
                return render(request, 'home.html')
            elif User.objects.filter(email=email1).exists():

                # print('email is  taken')
                messages.info(request,'email est déjà pris,veuillez changer')
                #return redirect('/')
                return render(request, 'home.html')
            else:
                user =User.objects.create_user(username=username, password= password1, email=email1)
                #print('user is created')
                messages.info(request,'vous vous êtes bien inscrit ')
                 # on enregistre le nouveau user
                user.save()
                return render(request, 'home.html')

        else:
            print('password is not matching')
        return redirect('/')
             

          
    else:
        return render(request, 'home.html')


@csrf_exempt
def signin(request):  
    if request.method == "POST":
        username= request.POST['username']
        password1 = request.POST['password']
        
        user = auth.authenticate(username=username, password=password1)

        if user is not None:

            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'les informations d \'identification invalides')
            return redirect('signin')
    else:
        return render(request, 'home.html')

    
def dashboard(request):
    return HttpResponseRedirect('/admin/')
    #return redirect(request, '/admin')


        