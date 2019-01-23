from django.urls import path
from libmgmt import views

# libapp/

app_name = 'libmgmt'

urlpatterns = [
  path('', views.showhome, name='home'),
  path('register/', views.showregister, name="register"),
  path('create-user/', views.createuser, name="createuser")
]
