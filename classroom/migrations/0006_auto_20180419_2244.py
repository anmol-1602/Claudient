# Generated by Django 2.0.4 on 2018-04-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_notice_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
