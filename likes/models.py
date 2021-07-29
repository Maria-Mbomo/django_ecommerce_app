from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class LikedItem(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    #if a user is deleted, all his liked objects disappear too
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object= GenericForeignKey()
    #type(product,vid,article), id
    #contenttypes nous permet de creer generic relationships
    #pour eviter que les app soient interconnectées à cause des imports

