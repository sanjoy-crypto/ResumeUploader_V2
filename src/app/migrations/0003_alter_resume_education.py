# Generated by Django 3.2.8 on 2021-10-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_resume_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.TextField(max_length=200),
        ),
    ]
