from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('books/', include('Books.urls')),
    path('category/', include('categories.urls')),
    path('transactions/', include('transactions.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)