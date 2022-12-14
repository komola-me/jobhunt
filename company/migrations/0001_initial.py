# Generated by Django 4.0.6 on 2022-08-01 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('company_name', models.CharField(max_length=256)),
                ('legal_name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=12)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/')),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkingField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_category', to='common.category')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_specialization', to='common.specialization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_work_field', to='company.companyprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=256)),
                ('salary_from', models.DecimalField(decimal_places=2, max_digits=15)),
                ('salary_to', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('published_date', models.DateField(auto_now=True)),
                ('employment_type', models.CharField(choices=[('full time', 'full time'), ('part time', 'part time'), ('internship', 'internship'), ('remote', 'remote')], max_length=15)),
                ('experience', models.IntegerField()),
                ('content', models.TextField()),
                ('is_premium', models.BooleanField(default=False)),
                ('is_urgent', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='company.companyprofile')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(related_name='tags', to='common.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_district', to='common.district')),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_region', to='common.region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_address', to='company.companyprofile', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
