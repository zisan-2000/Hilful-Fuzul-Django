from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books_count = models.IntegerField()
    image = models.ImageField(upload_to='publishers/', null=True, blank=True)

    def __str__(self):
        return self.name
