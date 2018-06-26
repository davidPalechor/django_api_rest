from django.db import models


class BasicInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tel = models.CharField(max_length=10, null=True)
    email = models.EmailField()
    address = models.CharField(max_length=100)


class AdditionalInfo(models.Model):
    id = models.AutoField(primary_key=True)
    art = models.CharField(max_length=255, null=True)
    movies = models.CharField(max_length=255, null=True)
    music = models.CharField(max_length=255, null=True)
    basic_info = models.ForeignKey(to='BasicInfo', on_delete=models.CASCADE)
