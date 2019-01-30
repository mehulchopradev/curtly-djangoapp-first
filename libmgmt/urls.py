from django.urls import path
from libmgmt import views, public_views
from django.views.generic import TemplateView

# libapp/

app_name = 'libmgmt'

urlpatterns = [
  path('', TemplateView.as_view(template_name='libmgmt/public/home.html'), name='home'),
  path('register/', TemplateView.as_view(template_name='libmgmt/public/register.html'), name="register"),
  path('create-user/', public_views.createuser, name="createuser"),
  path('auth-user/', public_views.authuser, name='authuser'),
  path('landing/', views.showlanding, name='landing'),
  path('book-details/<int:bookid>', views.bookdetails, name='bookdetails'),
  path('logout/', views.logout, name='logout'),
  path('issue-books/<int:bookid>', views.issuebook, name='issuebook'),
  path('return-books/<int:bookid>', views.returnbook, name='returnbook'),
  path('contact-us/', views.ContactUsView.as_view(), name='contactus'),
  path('sign-up/', public_views.RegisterView.as_view(), name='signup')
]
