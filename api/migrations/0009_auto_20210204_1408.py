# Generated by Django 3.1.5 on 2021-02-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210204_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='owner',
        ),
        migrations.AddField(
            model_name='contact',
            name='owner_id',
            field=models.IntegerField(null=True),
        ),
    ]
