# Generated by Django 2.2 on 2020-06-06 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20200606_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='tag',
            field=models.CharField(max_length=20),
        ),
    ]
