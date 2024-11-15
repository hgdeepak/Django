'''
URL module
'''
from django.urls import path
from django.views.generic import TemplateView
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name='home'),
    path("books/", BookListView.as_view(), name="bookslist"),
    path("books/new/", BookCreateView.as_view(), name="newbook"),
    path("books/<int:pk>", BookDetailView.as_view(), name="bookdetail"),
    path("books/edit/<int:pk>", BookUpdateView.as_view(), name="updatebook"),
    path("books/delete/<int:pk>", BookDeleteView.as_view(), name="deletebook"),
]
