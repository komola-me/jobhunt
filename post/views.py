from django.shortcuts import render
from rest_framework import generics
from post.serializers import PostSerializer
from post.models import Post

# Create your views here.
class NewsListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_news=True)[:4]


class BlogListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_blog=True)[:4]


class EventListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_event=True)[:4]
