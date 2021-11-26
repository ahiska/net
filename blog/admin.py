from django.contrib import admin

from .models import Article, Category, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'featured', 'status', 'created')
    list_editable = ('status', 'featured')
    list_filter = ('status', 'featured', 'created')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'active', 'date_added')
    list_filter = ('active', 'date_added')
    list_editable = ('active',)
    search_fields = ('name', 'email', 'body')

    # def approve_comments(self, queryset):
    #     queryset.update(active=True)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_header = "AHISKA.NET - Yönetim"
admin.site.site_title = "AHISKA.NET - Ahıska Türkleri'nin Sesi"
admin.site.index_title = "Yönetim Paneli"
