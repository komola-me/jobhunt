from django.db import models
from helpers.models import BaseModel
from common.models import User
from common.models import District, Specialization, Region, Category
from common.choices import GENDER, CURRENCY, STUDY_DEGREE, LEVELS


# Create your models here.
class Language(BaseModel):
    language = models.CharField(max_length=128)
    

class Skill(BaseModel):
    skill = models.CharField(max_length=128)


class WorkerProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='worker_profile')
    
    # main info
    #full_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=10, choices=GENDER)
    dob = models.DateField(auto_now=False)
    bio = models.TextField()
    image = models.ImageField(upload_to='worker/', blank=True)

    # contact info
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    # social media
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True) 


    # specific info
    expected_salary = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=5, choices=CURRENCY, default=1)

    # education = models.ManyToManyField(Education, related_name='worker_education')
    # experience = models.ManyToManyField(Experience, related_name='worker_experience')

    # skills
    skills = models.ManyToManyField(Skill, related_name='worker_skills', blank=True)

    is_freelancer = models.BooleanField(default=False)


class LanguageLevel(BaseModel):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='languages')
    level = models.CharField(max_length=16, choices=LEVELS)
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('language', 'worker'), ('language', 'level'))


class Address(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='worker_region')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='worker_district')
    user = models.ForeignKey(WorkerProfile, unique=True, on_delete=models.CASCADE, related_name='worker_pr')


class ProfessionalArea(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='worker_category')
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='worker_specialization')
    user = models.ForeignKey(WorkerProfile, unique=True, on_delete=models.CASCADE, related_name='employee_prof_area')


class Education(BaseModel):
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, related_name='education', default=1)
    institution = models.CharField(max_length=256)
    degree_of_study = models.CharField(max_length=50, choices=STUDY_DEGREE)
    major = models.CharField(max_length=128)
    month_start = models.CharField(max_length=15)
    year_start = models.PositiveSmallIntegerField()
    is_active_student = models.BooleanField(default=False)
    month_finish = models.CharField(max_length=15)
    year_finish = models.PositiveSmallIntegerField()
    about = models.TextField()


class Experience(BaseModel):
    worker = models.ForeignKey(WorkerProfile, on_delete=models.CASCADE, related_name='experience', default=1)
    position = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    month_start = models.CharField(max_length=15)
    year_start = models.PositiveSmallIntegerField()
    is_current = models.BooleanField(default=False)
    month_finish = models.CharField(max_length=15)
    year_finish = models.PositiveSmallIntegerField()
    about = models.TextField()

