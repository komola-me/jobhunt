# Generated by Django 4.0.6 on 2022-08-01 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='post/')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
                ('is_news', models.BooleanField(default=False)),
                ('is_blog', models.BooleanField(default=False)),
                ('is_event', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_createdby', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
