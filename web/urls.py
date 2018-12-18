from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('web/',views.keep_alive,name='alive'),
    path('test/',views.test,name='test'),
]