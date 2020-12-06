from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Post
import json
from django.utils import timezone



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

