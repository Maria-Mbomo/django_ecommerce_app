from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)
    
    
class TaggedItem(models.Model):
    #what tag applied to what object
    tag= models.ForeignKey(Tag, on_delete=models.CASCADE)
    #type(product,vid,article), id
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object= GenericForeignKey()
    #contenttypes nous permet de creer generic relationships
    #pour eviter que les app soient interconnectées à cause des imports















