# Generated by Django 3.1.5 on 2021-02-04 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210204_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adresses', to='api.contact'),
        ),
    ]
