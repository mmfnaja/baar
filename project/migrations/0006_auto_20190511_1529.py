# Generated by Django 2.2 on 2019-05-11 15:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_userinfo_access_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=200)),
                ('startdate', models.CharField(max_length=50)),
                ('enddate', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='realtime',
            old_name='userinfo',
            new_name='staffid',
        ),
        migrations.AddField(
            model_name='realtime',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.RenameModel(
            old_name='userinfo',
            new_name='staff',
        ),
        migrations.CreateModel(
            name='projectres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
                ('staffid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.staff')),
            ],
        ),
        migrations.CreateModel(
            name='projectasset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assetpath', models.CharField(max_length=200)),
                ('projectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='staffid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.staff'),
        ),
    ]
