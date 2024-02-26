from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'), 
    path('category/<slug:category_slug>/', views.home, name='category_wise_book'),
    path('accounts/', include('accounts.urls')),
    path('books/', include('Books.urls')),
    path('category/', include('categories.urls')),
    path('transactions/', include('transactions.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)