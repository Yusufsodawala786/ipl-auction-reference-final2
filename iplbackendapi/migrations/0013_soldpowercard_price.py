# Generated by Django 3.2.9 on 2022-03-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iplbackendapi', '0012_auto_20220324_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldpowercard',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]