# Generated by Django 2.1.1 on 2020-05-02 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tz',
            field=models.CharField(choices=[('i', 'i')], max_length=30),
        ),
    ]
