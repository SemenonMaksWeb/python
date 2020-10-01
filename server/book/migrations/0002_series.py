# Generated by Django 3.1.1 on 2020-09-13 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Серия книги',
                'verbose_name_plural': 'Серии книг',
                'db_table': 'series_book',
            },
        ),
    ]