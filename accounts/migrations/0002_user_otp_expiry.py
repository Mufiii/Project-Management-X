# Generated by Django 4.2.7 on 2024-02-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]