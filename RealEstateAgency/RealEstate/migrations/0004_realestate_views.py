# Generated by Django 4.1.7 on 2023-03-05 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate', '0003_alter_categories_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
