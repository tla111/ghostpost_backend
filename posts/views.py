from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def set_upvote(self, request, pk=None):
        post = Post.objects.get(id=pk)
        post.likes = post.likes + 1
        post.save()
        return Response({'status': 'ok', 'message': 'likes increase'})

    @action(detail=True, methods=['post'])
    def set_downvote(self, request, pk=None):
        post = Post.objects.get(id=pk)
        post.likes = post.likes - 1
        post.save()
        return Response({'status': 'ok', 'message': 'likes decreased'})



