from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books, name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('books/book_filter', views.book_filter, name='book_filter'),
    path('books/make_request', views.make_request, name='make_request'),
    path('books/request_history', views.request_history, name='request_history'),
    path('books/manage_books', views.manage_books, name='manage_books'),
]
