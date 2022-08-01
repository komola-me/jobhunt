from django.urls import path
from common.views import FeedbackListView

urlpatterns = [
    path('feedbacks/', FeedbackListView.as_view()),
]