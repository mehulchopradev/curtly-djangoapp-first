from django.contrib import admin
from libmgmt.models import Book, PublicationHouse, Review

class ReviewInline(admin.TabularInline):
  model = Review
  extra = 1

class BookAdmin(admin.ModelAdmin):
  fields = ('title','pages','price', 'publication')
  list_display = ('title', 'pages', 'price')
  search_fields = ('title',)
  list_filter = ('price', 'pages')
  inlines = (ReviewInline,)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(PublicationHouse)