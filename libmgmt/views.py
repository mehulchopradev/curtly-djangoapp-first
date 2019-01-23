from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def showhome(request):
  return render(request, 'libmgmt/public/home.html')

def showregister(request):
  return render(request, 'libmgmt/public/register.html')

def createuser(request):
  username = request.POST['username']
  password = request.POST['password']
  country = request.POST['country']
  gender = request.POST['gender']

  # TODO: save them in the database
  print(username)
  print(password)
  print(country)
  print(gender)

  return HttpResponseRedirect(reverse('libmgmt:home'))

  # A response consisting of the redirect url (response header) will be sent to the browser
  # Browser interprets the redirect url from the response header and makes another request to the redirect url