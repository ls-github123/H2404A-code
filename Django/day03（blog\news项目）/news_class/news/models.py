from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    