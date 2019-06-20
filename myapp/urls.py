from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
	path('home/', views.index, name = "index"),
	path('', views.index),
	path('search/', views.search, name = 'search'),

]