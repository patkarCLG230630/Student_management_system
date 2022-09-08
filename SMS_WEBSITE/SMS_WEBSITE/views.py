from django.shortcuts import render, redirect, HttpResponse
from app.Email_backend import EmailBackEnd
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from app.models import CustomUser,Registration
import random
from django.core.mail import send_mail
from SMS_WEBSITE import settings


def base(request):
    return render(request, 'base.html')


def LOGIN(request):

    return render(request, 'login.html')

def registration(request):
    s = "QWERTYUIOPASDGFHJKLZXCVBNMqwertyuioplkasjdhfg1234567890@#$%&"
    len_password = 7
    pw = "".join(random.sample(s, len_password))
    if request.method == "POST":
        last_name = request.POST.get("last_n ame")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        mobile_no = request.POST.get("mobile_no")
        email = request.POST.get("email")
        Registration.objects.create(last_name=last_name, first_name=first_name,middle_name=middle_name, gender=gender, dob=dob, mobile_no=mobile_no, email=email, password = pw )
        jitu = Registration.objects.get(password=pw)
        priya = jitu.id

        send_mail(f'Hello {first_name}',
                  f'your registration id is {priya} and password is {pw}',
                  settings.EMAIL_HOST_USER,
                  [email],
                  fail_silently=False,
                  )
        messages.success(
            request, f'Congratulations {first_name} your registration done succuessfully,your Registration id is {priya} and your password is {pw}')
        return render(request, 'registration.html')
    else:
        return render(request, 'registration.html')
    
    


def doLogin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get(
            'email'), password=request.POST.get('password'),)

        if user != None:
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('admin_home')
            elif user_type == '2':
                return HttpResponse('This is HOD Pannel')
            elif user_type == '3':
                return HttpResponse('This is Non_Teaching Pannel')
            elif user_type == '4':
                return HttpResponse('This is Teachers Pannel')
            elif user_type == '5':
                return HttpResponse('This is Student Pannel')
            elif user_type == '6':
                return HttpResponse('This is Parent Pannel')
            else:
                messages.error(request, 'Email and password are invalid !')
                return redirect('login')
        else:
            messages. error(request, 'Email and password  !')
            return redirect('login')

    
def doLogout(request):
    logout(request)
    return redirect('login')

def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    print(user)
    context = {
        'user': user
    }
    return render(request, 'profile.html',context)

def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')

        #print(first_name,last_name,email, username,password)
        print(profile_pic)

        try:
            #for custom user to get user id
            customuser = CustomUser.objects.get(id=request.user.id)
            
            customuser.first_name = first_name
            customuser.last_name = last_name

            #for change password
            if password != None and password != "":
                customuser.set_password(password)
                #if no one select profile pic
            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic

            customuser.save()
            #for success message
            messages.success(request, 'Your profile update successfully...!')
            return redirect('profile')
        except:
            #for error message
            messages.error(request, 'Failed to Update your Profile')
    return render (request, 'profile.html')