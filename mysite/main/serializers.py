from rest_framework import serializers 
from .models import BlogPost


class Blogpostserializer(serializers.Serializer):
    class Meta:
        model = BlogPost
        fields = [ 'id', 'title', 'content', 'publishedDate']