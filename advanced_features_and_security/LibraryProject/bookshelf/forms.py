# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description']  # Add any other fields if required

    # Optionally, add custom validation logic or field-level validation
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 3:
            raise forms.ValidationError("Author name must be at least 3 characters long.")
        return author
