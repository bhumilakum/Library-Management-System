# Generated by Django 2.1.3 on 2018-12-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20181220_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=models.IntegerField()),
        ),
    ]
