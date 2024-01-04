from django.contrib import admin
from .models import News, Image, Tag

# Register your models here.
admin.site.register(News)
admin.site.register(Image)
admin.site.register(Tag)