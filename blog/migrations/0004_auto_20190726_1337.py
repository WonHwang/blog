# Generated by Django 2.2.3 on 2019-07-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190726_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]
