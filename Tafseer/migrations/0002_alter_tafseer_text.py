# Generated by Django 4.0.4 on 2022-06-21 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tafseer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tafseer',
            name='text',
            field=models.FileField(upload_to=''),
        ),
    ]
