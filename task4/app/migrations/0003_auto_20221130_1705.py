# Generated by Django 3.1.3 on 2022-11-30 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20221114_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default=1, max_length=30, verbose_name='Ник пользователя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания ответа'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='avatars/default_pic.png', force_format=None, keep_meta=True, quality=100, scale=None, size=[50, 64], upload_to='avatars', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания вопроса'),
        ),
    ]
