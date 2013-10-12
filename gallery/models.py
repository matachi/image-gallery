from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    caption = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
