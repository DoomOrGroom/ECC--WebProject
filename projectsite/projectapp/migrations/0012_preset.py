# Generated by Django 3.2.7 on 2021-10-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0011_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preset',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('lights', models.JSONField()),
            ],
        ),
    ]
