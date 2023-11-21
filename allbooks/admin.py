from django.contrib import admin

# Register your models here.

from .models import Book, Chapter, Text

admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Text)

from .models import Collection

admin.site.register(Collection)
