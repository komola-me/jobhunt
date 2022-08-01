from django.urls import path
from post.views import BlogListView, NewsListView, EventListView

urlpatterns = [
    path('blog/', BlogListView.as_view()),
    path('news/', NewsListView.as_view()),
    path('event/', EventListView.as_view()),
]

