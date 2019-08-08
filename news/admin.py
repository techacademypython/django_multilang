from django.contrib import admin
from news import models


# Register your models here.

class ImageInline(admin.StackedInline):
    model = models.Images
    extra = 5


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


class NewsAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    fields = [
        "name_az", "name_en", "name_ru",
        "description_az", "description_en", "description_ru"
    ]


admin.site.register(models.Images)
admin.site.register(models.News, NewsAdmin)
admin.site.register(models.Article, ArticleAdmin)
