from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from libmgmt.models import Student, Book

# Create your views here.

def showhome(request):
  return render(request, 'libmgmt/public/home.html')

def showregister(request):
  return render(request, 'libmgmt/public/register.html')

def authuser(request):
  username = request.POST['username']
  password = request.POST['password']

  l = Student.objects.filter(username=username, password=password)
  if l:
    return HttpResponseRedirect(reverse('libmgmt:landing'))
  else:
    return HttpResponseRedirect(reverse('libmgmt:home'))

def showlanding(request):
  booklist = Book.objects.order_by('-price')
  context_data = {
    'booklist': booklist
  }
  return render(request, 'libmgmt/private/landing.html', context_data)

def bookdetails(request, bookid):
  # Get the Book object for the particular book asked for
  # id ????
  book = Book.objects.get(pk=bookid)
  context_data = {
    'book': book
  }
  return render(request, 'libmgmt/private/bookdetails.html', context_data)

def createuser(request):
  username = request.POST['username']
  password = request.POST['password']
  country = request.POST['country']
  gender = request.POST['gender']

  s = Student(username=username, password=password, gender=gender, country=country)

  try:
    s.save()
  except Exception:
    return HttpResponse('Error in registration')
  else:
    return HttpResponseRedirect(reverse('libmgmt:home'))

  '''print(username)
  print(password)
  print(country)
  print(gender)'''

  # A response consisting of the redirect url (response header) will be sent to the browser
  # Browser interprets the redirect url from the response header and makes another request to the redirect url