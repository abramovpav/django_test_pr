from django.contrib import admin

# Register your models here.
from articles.models import Article


class AdminArticle(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    readonly_fields = ('create_date', 'update_date')
    fieldsets = (
        (
            None,
            {
                'fields': ('title', 'body', 'author')
            }
        ),
        (
            'Additional Info',
            {
                'fields': ('create_date', 'update_date'),
                'classes': ('collapse', )
            }
        )
    )
    list_display = ('title', 'author', 'create_date')
    list_display_links = ('title', 'author', 'create_date')

admin.site.register(Article, AdminArticle)
