# Generated by Django 2.1.3 on 2018-12-17 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20181213_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]