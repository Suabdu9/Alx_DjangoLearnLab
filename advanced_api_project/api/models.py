from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
      # Represents an author. A single author can write multiple books.

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
     # Represents a book written by an author. Links to the Author model via a one-to-many relationship.
