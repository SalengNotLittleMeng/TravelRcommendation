from django.urls import re_path as url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^showmessage/', views.showmessage, name='showmessage'),

]