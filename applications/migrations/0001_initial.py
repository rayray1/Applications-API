# Generated by Django 2.0.4 on 2018-05-04 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.FileField(upload_to='')),
                ('package_name', models.CharField(max_length=200)),
                ('package_version_code', models.IntegerField()),
            ],
        ),
    ]