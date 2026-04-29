from django.contrib import admin
from django.urls import path,include

from .import views
urlpatterns = [
   path('',views.home),
   path('reg/',views.reg),
   path('formsave/',views.formsave),
   path('signin/',views.signin),
   path('signcheck/',views.signcheck),
   path('signout/',views.signout),
   path('reset_pass/',views.reset_pass),
   path('reset/',views.reset),
]
