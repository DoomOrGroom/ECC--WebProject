# Generated by Django 3.2.7 on 2021-10-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0012_preset'),
    ]

    operations = [
        migrations.AddField(
            model_name='preset',
            name='displays',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='preset',
            name='preset_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='preset',
            name='video_Wall',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='preset',
            name='workstations',
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='preset',
            name='lights',
            field=models.JSONField(null=True),
        ),
    ]
