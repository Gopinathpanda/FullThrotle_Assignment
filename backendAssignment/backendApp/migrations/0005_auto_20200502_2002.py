# Generated by Django 2.1.1 on 2020-05-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0004_auto_20200502_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
