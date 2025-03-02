from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponse,HttpResponseForbidden
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

def is_admin(user):
    return user.userprofile.role == 'Admin'

# Utility function to check if the user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Utility function to check if the user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        publication_year = request.POST.get('publication_year')
        
        author = get_object_or_404(Author, id=author_id)
        
        # Add the new book
        Book.objects.create(title=title, author=author, publication_year=publication_year)
        return redirect('book_list')  # Redirect to book list after adding
    
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author_id = request.POST.get('author_id')
        book.publication_year = request.POST.get('publication_year')
        book.save()
        
        return redirect('book_list')  # Redirect to book list after editing
    
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deleting
    
    return render(request, 'relationship_app/delete_book.html', {'book': book})