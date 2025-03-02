# bookshelf/forms.py
from django import forms
from .models import Book  # Adjust according to your model


class ExampleForm(forms.Form):  # or forms.ModelForm if you're using a model form
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField()

    # Optionally, add validation methods for the fields
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long.")
        return title
