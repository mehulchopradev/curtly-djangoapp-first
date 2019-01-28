from django.urls import path
from libmgmt import views, public_views

# libapp/

app_name = 'libmgmt'

urlpatterns = [
  path('', public_views.showhome, name='home'),
  path('register/', public_views.showregister, name="register"),
  path('create-user/', public_views.createuser, name="createuser"),
  path('auth-user/', public_views.authuser, name='authuser'),
  path('landing/', views.showlanding, name='landing'),
  path('book-details/<int:bookid>', views.bookdetails, name='bookdetails'),
  path('logout/', views.logout, name='logout'),
  path('issue-books/<int:bookid>', views.issuebook, name='issuebook'),
  path('return-books/<int:bookid>', views.returnbook, name='returnbook')
]
