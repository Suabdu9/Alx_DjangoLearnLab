from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)  # Get the Author by name
        books = Book.objects.filter(author=author)  # Get all books written by this author
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author {author_name} not found.")

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the Library by name
        books = library.books.all()  # Get all books associated with this library
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library {library_name} not found.")

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)  # Get the Library by name
        librarian = Librarian.objects.get(library=library)  # Access the associated Librarian using the one-to-one relationship
        print(f"The librarian for {library_name} is: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library {library_name} not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_name}.")

# Example usage
if __name__ == '__main__':
    # Example queries
    books_by_author('J.K. Rowling')
    books_in_library('Central Library')
    librarian_for_library('Central Library')
