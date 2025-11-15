from django import forms
from .models import Book
from .forms import ExampleForm


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
