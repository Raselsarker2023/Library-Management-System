from django.contrib import admin
from .models import Book, BorrowingHistory, BookReview, Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(BorrowingHistory)
admin.site.register(BookReview)
admin.site.register(Comment)
