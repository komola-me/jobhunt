from multiprocessing.dummy import JoinableQueue
from django.db import models
from helpers.models import BaseModel

# Create your models here.
class Post(BaseModel):
    title = models.CharField(max_length=256)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post/')

    date_time = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=256, blank=True, null=True)
    is_news = models.BooleanField(default=False)
    is_blog = models.BooleanField(default=False)
    is_event = models.BooleanField(default=False)

