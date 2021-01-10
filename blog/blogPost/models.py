from django.db import models


class BlogPost(models.Model):
    """ Blog post that user can write """
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
