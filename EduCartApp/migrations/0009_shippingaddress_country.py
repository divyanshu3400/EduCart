# Generated by Django 4.1 on 2022-09-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduCartApp', '0008_alter_tutorials_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
