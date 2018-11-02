# Generated by Django 2.1.1 on 2018-09-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20180928_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(blank=True, max_length=64, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='isbn',
            field=models.CharField(blank=True, max_length=32, verbose_name='ISBN'),
        ),
    ]
