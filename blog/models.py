from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=150)
    description = RichTextField()
    
