# -*- encoding: utf-8 -*-
from django.db import models


class Img(models.Model):
    img_url = models.ImageField(upload_to='photos/', blank=True, null=True)  # 指定图片上传路径，即media/photos/