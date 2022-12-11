from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# The Post model has a title, slug, author, updated_on, content, created_on, and status.
# The title and slug are defined as character fields of 200 characters each. The title is also set as
# unique.
# The author is a foreign key. This means that each post is written by a user and is related to a
# user.
# The updated_on and created_on fields are set to the current date and time.
# The status field is an integer field with choices defined in the STATUS variable.
# The content field is a text field.
# The slug field is also set as unique.
# The updated_on field is set to the current date and time.
# The status field is an integer field with choices defined in the STATUS variable.
# The content field is a text field.
# The slug field is also set as unique
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

