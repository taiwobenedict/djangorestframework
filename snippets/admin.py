from django.contrib import admin
from snippets.models import Snippet
from snippets.models import Author
# Register your models here.


admin.site.register(Snippet)
admin.site.register(Author)