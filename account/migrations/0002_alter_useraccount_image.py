# Generated by Django 4.2.10 on 2024-05-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(upload_to='images/user'),
        ),
    ]
