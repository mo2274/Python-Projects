from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """ Blog post that user can write """
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def __str__(self):
        if len(self.text) > 50:
            return f"{self.text[:50]}...."
        else:
            return self.text
