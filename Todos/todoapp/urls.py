from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('', signin),
    path('user/', user, name="user"),
    path('insert/',insert, name="insert"),
    path('signup/', signup_view, name = 'signup'),
    path('logout/', logout),
    path('delete/<id>', delete, name='delete'),
]