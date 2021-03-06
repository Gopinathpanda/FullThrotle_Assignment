# Generated by Django 2.1.1 on 2020-05-02 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0003_auto_20200502_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ok', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='activityperiods',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='backendApp.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='members',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='users', to='backendApp.Members'),
            preserve_default=False,
        ),
    ]
