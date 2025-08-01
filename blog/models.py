from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # ✅ এখন optional

    def __str__(self):
        return self.title
