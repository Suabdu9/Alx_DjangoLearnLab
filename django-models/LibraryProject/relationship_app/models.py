from django.db import models

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name  # This is to ensure the Author's name is returned when you call str(author)

# Book model with a ForeignKey to Author
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title  # Returns the book title when you call str(book)

# Library model with a ManyToManyField to Book
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name  # Returns the library name when you call str(library)

# Librarian model with a OneToOneField to Library
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name  # Returns the librarian's name when you call str(librarian)
