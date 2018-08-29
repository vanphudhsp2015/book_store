from django.shortcuts import render, redirect, HttpResponse

from .models import BookList
from django.db import connection
# Create your views here.
def index(request):
    books = BookList.objects.all().order_by('-id')
    context = {
        'books' : books
    }
    return render(request,'index.html',context)

def add_book(request):
    return render(request,'add_book.html')

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = BookList(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')

def delete(request,id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')

def edit(request,id):
    books = BookList.objects.get(pk=id)
    context = {
        'books':books
    }
    return render(request,'edit.html',context)

def update(request,id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')