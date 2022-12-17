from django.db import models
from django.contrib.auth.models import User


# A tuple of tuples.
STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Disabled"),
)

# STATUS_CAT = (
#    (0,"OFF"),
#    (1,"ON"),
#    (2,"Disabled"),
#)

#class Category(models.Model):
#    title = models.CharField(max_length=50)
#    description = models.TextField(blank=True)
#    slug = models.SlugField(max_length=50, unique=True)
#    updated_on = models.DateTimeField(auto_now= True)
#    status_cat = models.IntegerField(choices=STATUS_CAT, default=2)

#    class Meta:
#        ordering = ['-updated_on']

#    def __str__(self):
#        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    category = models.CharField(max_length=200, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=2)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

