# Generated by Django 3.2.9 on 2021-12-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.TextField()),
                ('nameofstudents', models.TextField()),
                ('numberofstudents', models.TextField()),
                ('projectname', models.TextField()),
                ('projecttype', models.TextField()),
                ('uploadproject', models.FileField(upload_to='')),
            ],
        ),
    ]
