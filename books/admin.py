from django.contrib import admin

from books.models import Books, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    inlines = (ReviewInline,)

