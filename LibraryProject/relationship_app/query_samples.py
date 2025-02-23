from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    # Replace these example names with actual names from your database
    author_name = "George Orwell"
    library_name = "Central Library"

    # Query all books by a specific author
    books_by_author = get_books_by_author(author_name)
    for book in books_by_author:
        print(f"Book by {author_name}: {book.title}")

    # List all books in a library
    books_in_library = get_books_in_library(library_name)
    for book in books_in_library:
        print(f"Book in {library_name}: {book.title}")

    # Retrieve the librarian for a library
    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"Librarian for {library_name}: {librarian.name}")
    else:
        print(f"No librarian found for {library_name}")
