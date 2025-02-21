from django.contrib import admin
from Blog.models import Tag, Post

# Register your models here.
admin.site.register(Tag)
admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

