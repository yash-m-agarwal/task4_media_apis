from django.db import models

class Images(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=1000, null=False)
    image = models.ImageField(upload_to='images/')
    createdby = models.CharField(max_length=255, null=False)
