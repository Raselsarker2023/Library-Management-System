from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>/', views.DetailBookView.as_view(), name='detail'),
    path('borrow/<int:id>/', views.BorrowBookView.as_view(), name='borrow'),
    path('return/<int:id>/', views.ReturnBookView.as_view(), name='return_book'),
]
