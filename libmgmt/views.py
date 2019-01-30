from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView
from libmgmt.models import Student, Book, BooksIssued
from datetime import date
from libmgmt.forms import ContactUsForm

# Create your views here.

def logout(request):
  # destroy the session and the data stored in the session for this request
  session_data = request.session
  session_data.flush() # destroy the session

  return HttpResponseRedirect(reverse('libmgmt:home'))

def showlanding(request):
  session_data = request.session
  if 'username' not in session_data:
    return HttpResponseRedirect(reverse('libmgmt:home'))

  studentid = session_data['userid']
  student = Student.objects.get(pk=studentid)

  booklist = Book.objects.order_by('-price')
  for book in booklist:
    if not book.noofcopies:
      book.cannotissue = True
    else:
      # students = book.student_set.all()
      '''for student in students:
        if student.id == studentid:
          book.bookissued = True # derived property to a model
          break
      else:
        # the book has not been issued to the currently logged in student
        if book.noofcopies == len(students):
          book.cannotissue = True
        else:
          book.cannotissue = False
          book.bookissued = False # derived property to a model'''
      try:
        bookissued = BooksIssued.objects.get(student=student, book=book, active='Y')
      except BooksIssued.DoesNotExist:
        students = BooksIssued.objects.filter(book=book, active='Y')

        if book.noofcopies == len(students):
          book.cannotissue = True
        else:
          book.cannotissue = False
          book.bookissued = False # derived property to a model'''
      else:
        book.bookissued = True

  context_data = {
    'booklist': booklist,
    'username': session_data['username']
  }
  return render(request, 'libmgmt/private/landing.html', context_data)

def bookdetails(request, bookid):
  # Get the Book object for the particular book asked for
  # id ????
  session_data = request.session
  if 'username' not in session_data:
    return HttpResponseRedirect(reverse('libmgmt:home'))

  book = Book.objects.get(pk=bookid)
  context_data = {
    'book': book,
    'username': session_data['username']
  }
  return render(request, 'libmgmt/private/bookdetails.html', context_data)

def issuebook(request, bookid):
  session_data = request.session
  if 'username' not in session_data:
    return HttpResponseRedirect(reverse('libmgmt:home'))

  book = Book.objects.get(pk=bookid)
  student = Student.objects.get(pk=session_data['userid'])

  # student.booksissued.add(book)
  bookissued = BooksIssued(student=student, book=book)
  bookissued.save()

  return HttpResponseRedirect(reverse('libmgmt:landing'))

def returnbook(request, bookid):
  session_data = request.session
  if 'username' not in session_data:
    return HttpResponseRedirect(reverse('libmgmt:home'))

  student = Student.objects.get(pk=session_data['userid'])
  book = Book.objects.get(pk=bookid)

  # student.booksissued.remove(bookid)

  bookissued = BooksIssued.objects.get(student=student, book=book)
  bookissued.returndate = date.today()
  bookissued.active = 'N'
  bookissued.save()

  return HttpResponseRedirect(reverse('libmgmt:landing'))

'''def showcontactus(request):
  if request.method == 'POST':
    c = ContactUsForm(request.POST)
    if c.is_valid():
      data = c.cleaned_data
      print(data)
      return HttpResponseRedirect(reverse('libmgmt:landing'))
  else:
    c = ContactUsForm()
  
  context_data = {
    'form': c
  }
  return render(request, 'libmgmt/private/contactus.html', context_data)'''

'''class ContactUsView(View):
  def get(self, request):
    c = ContactUsForm()
    context_data = {
      'form': c
    }

    return render(request, 'libmgmt/private/contactus.html', context_data)
  
  def post(self, request):
    c = ContactUsForm(request.POST)
    if c.is_valid():
      data = c.cleaned_data
      print(data)

      return HttpResponseRedirect(reverse('libmgmt:landing'))
    else:
      context_data = {
        'form': c
      }

      return render(request, 'libmgmt/private/contactus.html', context_data)'''

class ContactUsView(FormView):
  template_name = 'libmgmt/private/contactus.html'
  form_class = ContactUsForm

  def form_valid(self, form):
    data = form.cleaned_data
    print(data)

    return HttpResponseRedirect(reverse('libmgmt:landing'))
      