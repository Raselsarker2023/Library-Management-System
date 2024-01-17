from django import forms
from .models import Book, Comment

class PostForm(forms.ModelForm):
    class Meta: 
        model = Book
        fields = '__all__'
        #exclude = ['accounts']
        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']