from django.db import models
from django.contrib.contenttypes.models import ContentType



class Message(models.Model):
    name = models.CharField(max_length=200, null=False)
    fname = models.CharField(max_length=200,null=False)
    email = models.EmailField(null=False)
    mobile = models.CharField(max_length=200,null=False)
    body = models.TextField(max_length=400,null=False)

class Blog(models.Model):
    title = models.CharField(max_length=200, null=False)
    date = models.DateField()
    body = models.CharField(max_length=500, null=False)
    photo = models.ImageField(help_text='50x50px', blank=True, upload_to='worker/photo')


#class ListService(models.Model):
#    namecategory = models.CharField(max_length=200, null=False)

#class Service(models.Model):
#    name = models.CharField(max_length=200, null=False)
#    fname = models.CharField(max_length=200, null=False)
#    workArea = models.ForeignKey(ListService, on_delete=models.CASCADE, blank=True)
#    #workArea = models.CharField(max_length=200)
#    skill = models.CharField(max_length=200, null=False)
#    photo = models.ImageField(help_text='50x50px', blank=True, upload_to='worker/photo')





