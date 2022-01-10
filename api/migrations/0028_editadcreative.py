# Generated by Django 3.2.4 on 2022-01-10 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20211207_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditAdCreative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refreshToken', models.CharField(blank=True, max_length=500)),
                ('customer_id', models.CharField(max_length=500)),
                ('campaign_id', models.CharField(max_length=500)),
                ('new_headline_1', models.CharField(blank=True, max_length=30)),
                ('new_headline_2', models.CharField(blank=True, max_length=30)),
                ('new_headline_3', models.CharField(blank=True, max_length=30)),
                ('new_desc_1', models.CharField(blank=True, max_length=90)),
                ('new_desc_2', models.CharField(blank=True, max_length=90)),
            ],
        ),
    ]