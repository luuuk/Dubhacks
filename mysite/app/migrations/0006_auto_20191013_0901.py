# Generated by Django 2.2.3 on 2019-10-13 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20191013_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
