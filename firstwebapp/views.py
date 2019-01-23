from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
  # return HttpResponse('<html><body><b>Hello World</b></body></html>')
  return render(request, 'hello.html')

def home(request):
  return render(request, 'home.html')

def aboutus(request):
  return render(request, 'aboutus.html')

def contactus(request):
  # database code to retrieve the phone and the email
  phone = '9898945534'
  email = 'mehul@gmail.com'

  context_data = {
    'phone': phone,
    'email': email
  }

  return render(request, 'contactus.html', context_data)