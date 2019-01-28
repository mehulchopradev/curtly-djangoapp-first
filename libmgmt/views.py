from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from libmgmt.models import Student, Book

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
  booklist = Book.objects.order_by('-price')
  for book in booklist:
    if not book.noofcopies:
      book.cannotissue = True
    else:
      students = book.student_set.all()
      for student in students:
        if student.id == studentid:
          book.bookissued = True # derived property to a model
          break
      else:
        # the book has not been issued to the currently logged in student
        if book.noofcopies == len(students):
          book.cannotissue = True
        else:
          book.cannotissue = False
          book.bookissued = False # derived property to a model

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

  student.booksissued.add(book)

  return HttpResponseRedirect(reverse('libmgmt:landing'))

def returnbook(request, bookid):
  session_data = request.session
  if 'username' not in session_data:
    return HttpResponseRedirect(reverse('libmgmt:home'))

  student = Student.objects.get(pk=session_data['userid'])
  student.booksissued.remove(bookid)

  return HttpResponseRedirect(reverse('libmgmt:landing'))