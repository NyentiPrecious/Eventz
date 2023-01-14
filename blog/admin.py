from django.contrib import admin
from .models import Post
from home.models import Contact
from home.models import EventPage

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)

admin.site.register(Contact)

admin.site.register(EventPage)
# Register your models here.
