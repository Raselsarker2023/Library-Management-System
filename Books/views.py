from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils import timezone
from . import forms
from . import models
from django.views import View
from django.contrib import messages
from django.conf import settings
from django.views.generic import DetailView
from .models import Book, BorrowingHistory, BookReview
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import UserLibraryAccount


class DetailBookView(DetailView):
    model = models.Book
    pk_url_kwarg = 'id'
    template_name = 'details_book.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        
    

@method_decorator(login_required, name='dispatch')
class BorrowBookView(LoginRequiredMixin, DetailView):
    model = BorrowingHistory
    template_name = 'profile.html'
    context_object_name = 'borrow'
    
    def get(self, request, id, **kwargs):
        book = Book.objects.get(id=id)
        borrow = BorrowingHistory.objects.filter(user=request.user)

        if  self.request.user.account.balance >= book.borrowing_price:
            self.request.user.account.balance -= book.borrowing_price 
            self.request.user.account.save()
            
            BorrowingHistory.objects.create(user=request.user, book=book)
            
            messages.success(request, 'successfully! borrowing the book')
        else:
            messages.error(request, 'Insufficient balance to borrow the book.')
        return render(request, 'accounts/profile.html', {'borrowing_history' : borrow})



@method_decorator(login_required, name='dispatch')
class ReturnBookView(LoginRequiredMixin, View):
    # pk_url_kwarg = 'id'
    template_name = 'profile.html'
    
    def get(self, request, id, **kwargs):
        book = get_object_or_404(Book, id=id)
        borrowing_history, created = BorrowingHistory.objects.get_or_create(user=request.user, book=book)
        
        if created:
            self.request.user.account.balance += book.borrowing_price
            self.request.user.account.save()

            messages.success(request, 'Book returned successfully!')
        else:
            messages.error(request, 'No active borrowing record found for the book.')
        return redirect('profile')
