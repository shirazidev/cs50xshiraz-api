# Generated by Django 4.2.14 on 2024-07-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('photo', models.FileField(blank=True, null=True, upload_to='events')),
            ],
        ),
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=500)),
                ('icon', models.FileField(blank=True, null=True, upload_to='sponsors/icons')),
                ('photo', models.FileField(blank=True, null=True, upload_to='sponsors/photos')),
            ],
        ),
    ]