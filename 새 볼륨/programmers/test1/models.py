from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    text=models.TextField()

    def __str__(self):
        return self.title

    #write_date = models.DateTimeField(auto_now_add=True, blank=True)
