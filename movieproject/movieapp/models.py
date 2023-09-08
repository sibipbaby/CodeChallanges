from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.DateField()
    img = models.ImageField(upload_to="Gallery")

    def __str__(self):
        return '{}'.format(self.name)
