# Generated by Django 2.1.3 on 2018-12-12 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('isbn', models.CharField(help_text='13 Character ISBN number', max_length=13, verbose_name='ISBN')),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('a', 'available'), ('l', 'lended')], default='a', max_length=1)),
                ('author', models.ManyToManyField(to='library.Author')),
            ],
        ),
        migrations.CreateModel(
            name='BookLendDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_date', models.DateField(blank=True, null=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('charge', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('p', 'pending'), ('c', 'close')], default='p', max_length=1)),
                ('book', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='booklenddetail',
            name='reader',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.Reader'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='library.Category'),
        ),
    ]
