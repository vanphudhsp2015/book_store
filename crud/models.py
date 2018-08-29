from django.db import models

# Create your models here.
class BookList(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    author = models.CharField(max_length=150)

    def __tr__(self):
        return self.title