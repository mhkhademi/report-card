# Github.com/Rasooll
from django.urls import path
from . import views

app_name = 'tuition'

urlpatterns = [
    path('', views.home, name='tuition'),
    path('pay/', views.tuition, name='pay'),
    path('verify/', views.verify , name='verify'),
]
