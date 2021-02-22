from django.db import models

# Create your models here.

class Users(models.Model):

    uid = models.CharField('Uid метка человека', max_length=255)
    name = models.CharField('Имя человека', max_length=255)
    surname = models.CharField('Имя человека', max_length=255)

class SessionsToUser(models.Model):

     Member_ID = models.CharField('Мембер ID',max_length=255)
     allowed_members = models.BooleanField('Авторизован ли',default=False)
     user = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
     
