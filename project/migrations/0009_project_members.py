# Generated by Django 2.1.7 on 2019-05-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20190513_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(blank=True, null=True, related_name='members', to='project.staff'),
        ),
    ]
