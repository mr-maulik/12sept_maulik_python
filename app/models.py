from django.db import models

# Create your models here.


# class usersignup(models.Model):
#     firstname=models.CharField(max_length=20)
#     laststname=models.CharField(max_length=20)
#     gmail=models.EmailField()
#     pin=models.CharField(max_length=20)

class apoiment(models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField()
    time = models.DateTimeField()
    pho  = models.CharField(max_length=10)
    msg  = models.CharField(max_length=100)

    