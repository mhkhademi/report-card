from django.urls import path
from getscore import views

app_name = 'getscore'

urlpatterns = [
    path('', views.home, name='scorehome'),
    path('seescore/', views.seescore, name='seescore'),
    path('ranking/', views.ranking, name='ranking'),
]