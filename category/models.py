from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.TextField()
    category_image = models.ImageField(upload_to='photos/category', null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name
