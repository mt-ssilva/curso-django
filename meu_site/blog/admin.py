from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('titulo','autor','publicado','status',)
    list_filter = ('status','publicado','criado','autor',)
    date_hierarchy = 'publicado'
    search_fields = ('titulo','conteudo')
    prepopulated_fields = {'slug':('titulo',)}


# Register your models here.
