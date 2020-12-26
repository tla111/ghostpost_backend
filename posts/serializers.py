from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
          'id', 'content', 'name_post', 'submission_time', 'likes', 'dislikes'
        ]
