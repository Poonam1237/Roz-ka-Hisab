from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('dashboard/',views.dashboard,name='dashboard'),

    path('member/<str:mname>',views.member,name='member'),
    path('account/<str:aname>',views.account,name='account'),

]