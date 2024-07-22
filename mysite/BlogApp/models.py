from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=100)
    bio = models.TextField(null=False, blank=True)


class Category(models.Model):

    name = models.CharField(max_length=40)


class Tag(models.Model):

    name = models.CharField(max_length=20)


class Article(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, related_name='tag')

    def get_absolute_url(self,):
        return reverse('BlogApp:article_detail', kwargs={'pk': self.pk})
    