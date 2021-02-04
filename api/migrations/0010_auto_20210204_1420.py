# Generated by Django 3.1.5 on 2021-02-04 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_auto_20210204_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='owner_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
    ]