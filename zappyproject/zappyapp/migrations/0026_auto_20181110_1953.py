# Generated by Django 2.1.1 on 2018-11-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0025_auto_20181102_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Products/1-1.jpg', upload_to='Products'),
        ),
    ]