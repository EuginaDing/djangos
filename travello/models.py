from django.db import models

# Create your models here.
class Course(models.Model):
    #id:int
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    desc_enroll=models.IntegerField()
    special=models.BooleanField()
    price=models.IntegerField()