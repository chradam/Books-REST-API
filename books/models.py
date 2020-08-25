from django.db import models
# Create your models here.


class Book(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    published_date = models.CharField(max_length=4)
    categories = models.ManyToManyField('Category')
    average_rating = models.DecimalField(blank=True, null=True, max_digits=2, decimal_places=1)
    ratings_count = models.IntegerField(blank=True, null=True)
    thumbnail = models.URLField(max_length=255)

    # class Meta:
    #     unique_together = (('title', 'published_date'),)

    def __str__(self):
        return self.title


class Author(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    objects = models.Manager()

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
