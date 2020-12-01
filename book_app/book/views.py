from django.shortcuts import render
from .models import Book
# Create your views here.
def index(request):
	books = Book.objects.order_by('pub_date')
	context = {
	'books':books
	}
	return render(request, 'index.html',context)