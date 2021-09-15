from django.urls import path
from .import views

urlpatterns=[

    path('log/',views.loginview,name='login'),
    path('logo/',views.logoutview,name='logout'),
    path('reg/',views.registerview,name='register')
]