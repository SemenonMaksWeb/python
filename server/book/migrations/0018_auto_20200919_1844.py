# Generated by Django 3.1.1 on 2020-09-19 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0017_auto_20200917_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Author',
            field=models.ManyToManyField(related_name='_author', to='book.author', verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Editor',
            field=models.ManyToManyField(db_table='book_editor', related_name='_editor', to='book.author', verbose_name='Переводчик книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Genre',
            field=models.ManyToManyField(to='book.genre', verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.publisher', verbose_name='Издатель книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.series', verbose_name='Серия книги'),
        ),
    ]