# Generated by Django 2.2 on 2019-05-05 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginid', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=30)),
                ('competency', models.CharField(max_length=30)),
                ('access_level', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='realtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.userinfo')),
            ],
        ),
    ]
