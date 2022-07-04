from django.db import models

# Create your models here.
class blogs(models.Model):
    Image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=500,null=True)
    description=models.CharField(max_length=1200,null=True)
    date=models.DateField(auto_now_add=True,null=True)
    likes=models.IntegerField(default=0)