# Generated by Django 4.2.10 on 2024-05-07 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.ImageField(upload_to='images/user'),
        ),
    ]