### resources app models


from django.db import models
from django.utils import timezone  # for tz aware dates
from django.urls import reverse # for category url


class Resource_Category(models.Model):
    #   Categories of Resources

    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=75, unique=True)

    class Meta:
        ordering = ['category']

        #   for admin names
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        #   model text listing
        return self.category
    
    def get_absolute_url(self):
        return reverse('resources:resources_by_category', args=[self.slug])

class Resource(models.Model):
    #   Categories of Questions

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=75, unique=True)
    description = models.TextField()
    location = models.URLField()

    category = models.ForeignKey(
        #   category
        Resource_Category,
        on_delete=models.CASCADE,
        related_name="resources",
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        #   model text listing
        return self.name