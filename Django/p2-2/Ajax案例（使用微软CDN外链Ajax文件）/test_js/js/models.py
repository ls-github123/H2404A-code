from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField(),
    gender = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'member'
    
    def __str__(self):
        return self.username
    