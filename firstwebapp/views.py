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
  return render(request, 'contactus.html')