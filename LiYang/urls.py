from django.urls import path

from LiYang import views

app_name = 'LiYang'
urlpatterns = [
    path('', views.index, name='index'),
]
