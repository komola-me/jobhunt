from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from common.models import Feedback
from common.serializers import FeedbackSerializer

# Create your views here.
class FeedbackListView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

