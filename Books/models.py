from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True) 
    borrowing_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='Books/media/uploads/', blank = True, null = True)
    
    def __str__(self):
        return self.title
    

class BorrowingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(default=timezone.now())
    returned_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"Review by {self.user.first_name}"

class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=100)
    
    def __str__(self):
        return f"Review by {self.user.name}"
    
    
class Comment(models.Model):
    post = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"