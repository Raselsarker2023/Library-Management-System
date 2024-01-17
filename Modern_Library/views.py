from django.views.generic import ListView
from Books.models import Book
from categories.models import Category

class HomeView(ListView):
    model = Book
    template_name = 'home.html'   
    context_object_name = 'data'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            return Book.objects.filter(category=category)
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
