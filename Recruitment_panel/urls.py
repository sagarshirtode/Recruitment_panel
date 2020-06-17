"""Recruitment_panel URL Configuration

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
from django.conf.urls import include, url
from Recruit import views

urlpatterns = [
    # JOBSEEKER
    path('admin/', admin.site.urls),
    path('',views.entry),
    path('logincheck', views.logincheck),
    path('jobseekerRegistration',views.jobseekerRegistration),
    path('forgot', views.forgot ),
    path('jobseekerhome', views.jobseekerhome),
    path('post', views.post),
    path('newapplication/<int:id>',views.newapplication),
    path('dashboard',views.dashboard),
    path('about', views.about),
    path('createApplication', views.createApplication),
    path('jobseekerRegi',views.jobseekerRegi),
    path('logout',views.logout),
    path('status/<str:userName>',views.status),
    path('appsubmit',views.applicationsubmit),
    # ADMIN PART

    path('ad007',views.ad007),#NAV
    path('adminHome', views.adminHome),#NAV
    path('newPost', views.newPost),#NAV
    path('postinput',views.postinput),
    path('report',views.report),
    path('dashboard',views.dashboard),
    path('allapplicatins',views.allapplicatins),
    path('interviewAnalysis',views.interviewAnalysis),
    path('schedule',views.schedule),
    path('scheduleDelete',views.scheduleDelete),
    path('ApplicationForm/<int:application_id>',views.viewForm),
    path('addpost',views.addpost),
    path('postdelete/<str:post_name>',views.postdelete),
    path('livepdelete/<int:id>',views.livepdelete),
    path('addnotic',views.addnotic),
    path('notice',views.noticeShow),
    path('insertpoints',views.insertpoints),
    path('noticeDelete',views.noticeDelete),
    path('alctri',views.alctri)
    # path('totalanapoint/<int:j_id>',views.totalanapoint)
    # path('search',views.search, name='search')
] 
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)