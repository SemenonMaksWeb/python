# Generated by Django 3.1.1 on 2020-09-16 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20200915_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='Series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.series'),
        ),
    ]
