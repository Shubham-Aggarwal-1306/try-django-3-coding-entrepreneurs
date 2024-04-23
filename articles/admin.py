from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'timestamp', 'updated', 'publish']
    search_fields = ['id', 'title']

admin.site.register(Article, ArticleAdmin)