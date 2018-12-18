from django.shortcuts import render
from library.models import Book, Category, Author, BookLendDetail
from django.views import generic
from . import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date

def index(request):
     return render(request, 'index.html')

class BookDetailView(generic.DetailView):
    model = Book

def books(request):
    context = []
    search_key = str(request.GET.get('search_key', "")).strip()
    filter_key = str(request.GET.get('filter_key', "")).strip()

    if filter_key == 'firstname':
        context = Book.objects.filter(author__firstname__contains = search_key)
    elif filter_key == 'lastname':
        context = Book.objects.filter(author__lastname__contains = search_key)
    elif filter_key == 'title':
        context = Book.objects.filter(title__contains = search_key)
    elif filter_key == 'isbn':
        context = Book.objects.filter(isbn = search_key)
    else:
        context = Book.objects.all()

    paginator = Paginator(context, 6)
    page = request.GET.get('page')

    try:
        context = paginator.page(page)
    except PageNotAnInteger:
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)

    filter_list = [
        {'value': 'all', 'name': 'All'},
        {'value': 'firstname', 'name': 'Author Firstname'},
        {'value': 'lastname', 'name': 'Author Lastname'},
        {'value': 'title', 'name': 'Book Title'},
        {'value': 'isbn', 'name': 'ISBN'}
    ]
    return render(request, 'books.html', {'context': context, 'filter_list': filter_list})

@login_required
def book_filter(request):
    context = []
    search_key = str(request.GET.get('search_key', "")).strip()
    filter_key = str(request.GET.get('filter_key', "")).strip()

    if filter_key == 'firstname':
        context = Book.objects.filter(author__firstname__contains = search_key)
    elif filter_key == 'lastname':
        context = Book.objects.filter(author__lastname__contains = search_key)
    elif filter_key == 'title':
        context = Book.objects.filter(title__contains = search_key)
    elif filter_key == 'isbn':
        context = Book.objects.filter(isbn = search_key)
    elif filter_key == 'status_a':
        context = Book.objects.filter(status = 'a', title__contains = search_key)
    elif filter_key == 'status_l':
        context = Book.objects.filter(status = 'l', title__contains = search_key)
    else:
        context = Book.objects.all()

    paginator = Paginator(context, 6)
    page = request.GET.get('page')

    try:
        context = paginator.page(page)
    except PageNotAnInteger:
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)

    filter_list = [
        {'value': 'all', 'name': 'All'},
        {'value': 'firstname', 'name': 'Author Firstname'},
        {'value': 'lastname', 'name': 'Author Lastname'},
        {'value': 'title', 'name': 'Book Title'},
        {'value': 'isbn', 'name': 'ISBN'},
        {'value': 'status_a', 'name': 'Books Available'},
        {'value': 'status_l', 'name': 'Books Lent'}
    ]
    return render(request, 'book_filter.html', {'context': context, 'filter_list': filter_list})


@login_required
def make_request(request):
    data = Book.objects.filter(status = 'a')

    if request.method == 'POST':
        req_book_title = request.POST.get('book_list')

        book_detail = Book.objects.get(title=req_book_title)
        data = BookLendDetail(book = book_detail, reader = request.user, req_date = date.today(), charge = 0)
        data.save()

        return render(request, 'request_history.html')


    return render(request, 'make_request.html', {'context': data})

@login_required
def request_history(request):
    req_pending = BookLendDetail.objects.filter(reader = request.user, status = 'p')
    req_close =  BookLendDetail.objects.filter(reader = request.user, status = 'c')
    req_lending =  BookLendDetail.objects.filter(reader = request.user, status = 'l')

    context = {
        'p': req_pending,
        'c': req_close,
        'l': req_lending
    }
    return render(request, 'request_history.html', {'context' : context})

@login_required
def manage_books(request):
    context = []
    search_key = str(request.GET.get('search_key', "")).strip()
    filter_key = str(request.GET.get('filter_key', "")).strip()

    if filter_key == 'firstname':
        context = Book.objects.filter(author__firstname__contains = search_key)
    elif filter_key == 'lastname':
        context = Book.objects.filter(author__lastname__contains = search_key)
    elif filter_key == 'title':
        context = Book.objects.filter(title__contains = search_key)
    elif filter_key == 'isbn':
        context = Book.objects.filter(isbn = search_key)
    elif filter_key == 'status_a':
        context = Book.objects.filter(status = 'a', title__contains = search_key)
    elif filter_key == 'status_l':
        context = Book.objects.filter(status = 'l', title__contains = search_key)
    else:
        context = Book.objects.filter(title__contains = search_key)

    paginator = Paginator(context, 6)
    page = request.GET.get('page')

    try:
        context = paginator.page(page)
    except PageNotAnInteger:
        context = paginator.page(1)
    except EmptyPage:
        context = paginator.page(paginator.num_pages)

    filter_list = [
        {'value': 'all', 'name': 'All'},
        {'value': 'firstname', 'name': 'Author Firstname'},
        {'value': 'lastname', 'name': 'Author Lastname'},
        {'value': 'title', 'name': 'Book Title'},
        {'value': 'isbn', 'name': 'ISBN'},
        {'value': 'status_a', 'name': 'Books Available'},
        {'value': 'status_l', 'name': 'Books Lent'}
    ]

    return render(request, 'manage_books.html', {'context' : context, 'filter_list': filter_list})
