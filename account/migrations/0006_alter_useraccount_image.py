# Generated by Django 4.2.10 on 2024-05-17 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.URLField(),
        ),
    ]
