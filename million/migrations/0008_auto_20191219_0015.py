# Generated by Django 2.2.6 on 2019-12-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('million', '0007_auto_20191219_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='date',
            field=models.DateField(blank=True, default='', max_length=20, null=True, verbose_name='dateofadd'),
        ),
    ]
