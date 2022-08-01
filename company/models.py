from django.db import models
from common.models import User, Tag, Specialization, District, Region, Category
from helpers.models import BaseModel
from common.choices import EMPLOYMENT_TYPE

# Create your models here.
class CompanyProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=256)
    legal_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=12)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    email = models.EmailField()

    bio = models.TextField()


class Vacancy(BaseModel):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='author')
    salary_from = models.DecimalField(max_digits=15, decimal_places=2)
    salary_to = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    published_date = models.DateField(auto_now=True)
    employment_type = models.CharField(max_length=15, choices=EMPLOYMENT_TYPE)
    experience = models.IntegerField()

    content = models.TextField()

    tag = models.ManyToManyField(Tag, related_name='tags')

    is_premium = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    # filter: ordinary vacancies, all vacancies
    # filter: time_period: 24hours, 3days, 7days, 14days, all the time
    # filter: salary: doesn't matter, up to 3mln, 3-7mln, 7-15mln, 15+mln
    # filter: location: region, district


class CompanyAddress(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='company_region')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='company_district')
    user = models.ForeignKey(CompanyProfile, unique=True, on_delete=models.CASCADE, related_name='company_address')


class WorkingField(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='company_category')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='company_specialization')
    user = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE, related_name='company_work_field')

