from django import forms
from snippets.models import Author, Snippet

class SnippetForm(forms.ModelForm):
    
    class Meta:
        model = Snippet
        exclude = ['author']
        fields = ("__all__")

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("__all__")