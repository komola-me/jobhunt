from rest_framework import generics
from worker.serializers import WorkerProfileSerializer, LanguageLevelSerializer
from worker.models import WorkerProfile, LanguageLevel

# Create your views here.
class WorkerProfileListView(generics.ListCreateAPIView):
    queryset = WorkerProfile.objects.all().prefetch_related('specialization__category')
    serializer_class = WorkerProfileSerializer


class WorkerCreateView(generics.CreateAPIView):
    queryset = WorkerProfile.objects.all().prefetch_related('worker_spec')
    serializer_class = WorkerProfileSerializer