from django.contrib import admin
from blog.models import Post
from organizer.models import Tag, Startup, NewsLink
# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Startup)
admin.site.register(NewsLink)
