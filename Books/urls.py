from django.urls import path, include
from . import views
from .views import DetailBookView, ReturnBookView, BorrowBookView
urlpatterns = [
    path('details/<int:id>/', views.DetailBookView.as_view(), name='detail'),
    path('borrow/<int:id>/', views.BorrowBookView.as_view(), name='borrow'),
    path('return/<int:id>/', views.ReturnBookView.as_view(), name='return_book'),
]
