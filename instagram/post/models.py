# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, related_name='createdBy', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, through= 'PostUserLike', related_name='likes')

class PostUserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_datetime = models.DateTimeField(auto_now=True)
    