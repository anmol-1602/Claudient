# Generated by Django 2.0.4 on 2018-04-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0012_usermoreinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermoreinfo',
            name='designation',
            field=models.CharField(choices=[(1, 'Teacher'), (2, 'Student')], max_length=10),
        ),
    ]
