from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('web/',views.keep_alive,name='alive'),
    path('test/',views.test,name='test'),
    path('get_data/',views.get_data,name='get_data'),
    path('today_data/',views.today_data,name='today_data'),
]