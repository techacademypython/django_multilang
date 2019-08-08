from django.db import models


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Images(models.Model):
    news = models.ForeignKey(Article, related_name="images", on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to="news/")
    image_token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.image.name}"
