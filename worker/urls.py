from django.urls import path
from worker.views import WorkerProfileListView


urlpatterns = [
    path('worker/', WorkerProfileListView.as_view()),
]