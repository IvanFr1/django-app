from django.contrib import admin
from .models import Author, Category, Tag, Article

# Register your models here.


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = "id", "title", "content", "pub_date",