# Generated by Django 4.2.5 on 2023-10-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mySelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myself',
            name='admNo',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='myself',
            name='nickName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
