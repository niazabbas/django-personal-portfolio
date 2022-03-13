from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField('portfolio/images/')
    urls = models.URLField(blank=True)

    def _str_(self):
            return self.title
