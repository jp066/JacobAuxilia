# Generated by Django 5.1.3 on 2024-11-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='feedback_attachments/'),
        ),
    ]
