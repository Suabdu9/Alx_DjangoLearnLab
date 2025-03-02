from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book  # Assuming you have a Book model
from django.http import HttpResponseForbidden
from .forms import ExampleForm

# Example view to list books (only accessible by users with 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Get all books
    return render(request, 'bookshelf/book_list.html', {'books': books})
