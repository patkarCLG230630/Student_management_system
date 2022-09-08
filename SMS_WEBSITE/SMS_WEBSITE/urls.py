"""SMS_WEBSITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Admin_view, HOD_views, Non_teaching, Teachers_view, student_views, Parent_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
#########################################################################
    #Login Path
    path('',views.LOGIN,name='login'),
    path('doLogin/',views.doLogin, name='doLogin'),
    path('doLogout/',views.doLogout, name='doLogout'),

    #Registration path
    path('registration/',views.registration, name='registration'),
 
    #Profile Update
    path('profile',views.profile, name='profile'),  
    path('profile/update',views.profile_update, name='profile_update'),  
#########################################################################
    #this is for Admin urls
    #For Admin Page
    path('admin/home', Admin_view.home, name='admin_home'),
    path('admin/student/add', Admin_view.addstudent, name='addstudent'),

##########################################################################
    #this is for student urls
    path('student/home',student_views.home,name='home'),
    path('student/studentbase',student_views.studentbase,name='studentbase'),
    

]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)