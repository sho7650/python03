# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class softlayer_api(models.Model):
    username     = models.CharField(max_length=64)
    api_key      = models.CharField(max_length=255)
    endpoint_url = models.CharField(max_length=1024)

class CustomUser(AbstractUser):
    softlayer_id = models.IntegerField(blank=True, null=True)

