# Generated by Django 3.2 on 2021-05-02 15:00

from django.db import migrations, models
import gag.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=gag.helpers.UploadTo('profile')),
        ),
    ]
