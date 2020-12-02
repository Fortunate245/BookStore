from django.shortcuts import render,redirect
from .models import Book
# Create your views here.
def index(request):
	books = Book.objects.order_by('pub_date')
	context = {
	'books':books
	}
	if request.method=='POST':
			author = request.POST.get('author')
			name = request.POST.get('name')
			isbn = request.POST.get('isbn')
			url = request.POST.get('url')
			new_book = Book(name=name,author=author,isbn=isbn,book_url=url)
			new_book.save()

			return redirect('/')

		

		
	return render(request, 'index.html',context)