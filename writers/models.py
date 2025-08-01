from django.db import models

class Writer(models.Model):
    name = models.CharField(max_length=100)
    books_count = models.IntegerField()
    image = models.ImageField(upload_to='writers/', null=True, blank=True)

    def __str__(self):
        return self.name
