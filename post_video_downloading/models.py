# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model
import uuid
import os

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    filename = instance.name + "_" + filename
    # return the whole path to the file
    return os.path.join('photos', filename)


class User(models.Model):
    username=models.CharField(max_length=16)
    password=models.CharField(max_length=32)


class Message(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Image(models.Model):
    name = models.CharField(max_length=150, null=True)
    file = models.ImageField(upload_to=user_directory_path)
    # message = models.ForeignKey(Message, on_delete=models.CASCADE)

