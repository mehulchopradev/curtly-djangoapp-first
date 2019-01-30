from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from libmgmt.models import Student, Book
from django.views.generic.edit import FormView
from libmgmt.forms import RegisterForm

'''def showhome(request):
  return render(request, 'libmgmt/public/home.html')'''

'''def showregister(request):
  return render(request, 'libmgmt/public/register.html')'''

def authuser(request):
  username = request.POST['username']
  password = request.POST['password']

  l = Student.objects.filter(username=username, password=password)
  if l:
    # valid user
    # remember logged in user specific data for the entire time the user is logged in
    # username needs to be remembered
    # data to be remembered must be client specific
    # http sessions

    request.session['username'] = username
    request.session['userid'] = l[0].id

    return HttpResponseRedirect(reverse('libmgmt:landing'))
  else:
    return HttpResponseRedirect(reverse('libmgmt:home'))

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

class RegisterView(FormView):
  template_name = 'libmgmt/public/register.html'
  form_class = RegisterForm

  def form_valid(self, form):
    '''data = form.cleaned_data

    s = Student(**data)

    try:
      s.save()
    except Exception:
      return HttpResponse('Error in registration')
    else:
      return HttpResponseRedirect(reverse('libmgmt:home'))'''

    try:
      s = form.save()
    except Exception:
      return HttpResponse('Error in registration')
    else:
      return HttpResponseRedirect(reverse('libmgmt:home'))