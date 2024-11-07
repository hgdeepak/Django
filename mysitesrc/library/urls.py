'''
URL module
'''
from django.urls import path
from django.views.generic import TemplateView
from .views import BookListView, BookDetailView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name='home'),
    path("books/", BookListView.as_view(), name="bookslist"),
    path("books/<int:pk>", BookDetailView.as_view(), name="bookdetail"),
]
