from django import forms
from book.models import Book

class FromBook(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','author','description','genre','isbn','publication_date']


