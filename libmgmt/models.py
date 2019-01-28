from django.db import models
from datetime import date

# Create your models here.
class PublicationHouse(models.Model):
  # id
  name = models.CharField(null=False, max_length=50)
  ratings = models.IntegerField(null=True)

  # book_set

  # Book - One to many

  def __str__(self):
    return self.name

class Book(models.Model):
  # id
  title = models.CharField(null=False, max_length=30)
  price = models.FloatField(null=True)
  pages = models.IntegerField(null=False)
  noofcopies = models.IntegerField(null=False, default=0)
  publication = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE) # fetched eagerly

  # review_set # fetched lazily
  # student_set

  # Publication - Many to One
  # Review - One to Many
  # Student - One to Many

  def __str__(self):
    return self.title

class Review(models.Model):
  reviewer = models.CharField(null=False, max_length=50)
  description = models.CharField(null=False, max_length=200)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  # Book - Many to One

class Student(models.Model):
  # id
  username = models.CharField(null=False, max_length=25)
  password = models.IntegerField(null=False)
  country = models.CharField(null=False, max_length=5)
  gender = models.CharField(null=True, max_length=1)
  books_issued = models.ManyToManyField(Book, through='BooksIssued')

  # Book - One to many

class BooksIssued(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  active = models.CharField(null=False, default='Y', max_length=1)
  issuedate = models.DateField(null=False, default=date.today())
  returndate = models.DateField(null=True)