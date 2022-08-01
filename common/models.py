from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from helpers.models import BaseModel


# Create your models here.
class User(AbstractUser):
    INVALID_CODE = "######"

    USER_TYPE_CHOICES = (
      (1, 'company'),
      (2, 'worker'),
  )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=2)

    full_name = models.CharField(_("full name"), max_length=256)


    created_at = models.DateTimeField(_("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("date updated"), auto_now=True)

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Tag(BaseModel):
    title = models.CharField(max_length=128)


class Category(BaseModel):
    title = models.CharField(max_length=128)

    # vacancy_count, salary min-max, icons of companies 


class Specialization(BaseModel):
    specialization = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Region(BaseModel):
    title = models.CharField(max_length=128, unique=True)


class District(BaseModel):
    district = models.CharField(max_length=128)


class Feedback(BaseModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

