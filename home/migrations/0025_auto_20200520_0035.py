# Generated by Django 2.2 on 2020-05-19 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20200519_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='questioner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questioner', to='home.UserProfile'),
        ),
    ]
