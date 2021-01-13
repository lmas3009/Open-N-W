from django.db import models

# Create your models here.


class News(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    title = models.CharField(max_length=220)
    description = models.CharField(max_length=220)
    url = models.CharField(max_length=220)
    urlToImage = models.CharField(max_length=220)
    publishedAt = models.CharField(max_length=120)
    content = models.CharField(max_length=420)

    def __str__(self):
        return self.title
