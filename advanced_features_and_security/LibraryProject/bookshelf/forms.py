# bookshelf/forms.py

from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField()

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title

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
