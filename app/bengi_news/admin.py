from django.contrib import admin
from .models import News, Image, Tag


class ImageInline(admin.TabularInline):  # or admin.StackedInline
    model = Image
    extra = 1  # number of extra forms to display


class NewsAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main_image":
            if request._obj_ is not None:
                kwargs["queryset"] = Image.objects.filter(news=request._obj_)
            else:
                kwargs["queryset"] = Image.objects.none()

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_form(self, request, obj=None, **kwargs):
        # just save obj reference for future processing in Inline
        request._obj_ = obj
        return super().get_form(request, obj, **kwargs)


# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
