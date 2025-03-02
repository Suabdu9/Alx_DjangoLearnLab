from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .models import Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show the details of a specific library
class LibraryDetailView(DetailView): # type: ignore
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template to render the library details
    context_object_name = 'library'  # Context variable name for the template

    # This view will show the books available in the selected library
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # Get the specific library object
        context['books'] = library.books.all()  # Add all books associated with the library to the context
        return context
    
# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create the user
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Home view for authenticated users
@login_required
def home(request):
    return render(request, 'relationship_app/home.html')