# Generated by Django 2.1.3 on 2018-12-22 17:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_auto_20181222_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character ISBN number', max_length=13, validators=[django.core.validators.RegexValidator('^[0-9]*$', 'Only  numeric characters are allowed.')], verbose_name='ISBN'),
        ),
    ]
