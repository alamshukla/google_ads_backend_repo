# Generated by Django 3.2.4 on 2022-06-17 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_createsmartcampaign_mytoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignsettings',
            name='mytoken',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]