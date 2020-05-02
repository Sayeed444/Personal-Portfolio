from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=222)
    description = models.TextField()
    image = models.ImageField(upload_to='blog',blank=True,default='OTF.png')
    date = models.DateField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        ordering =['-datetime']

    def textfild(self):
        return self.description[:350] + '... ... ... !'