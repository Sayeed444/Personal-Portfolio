from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=222)
    description = models.CharField(max_length=222)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
