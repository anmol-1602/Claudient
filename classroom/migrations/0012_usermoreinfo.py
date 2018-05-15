# Generated by Django 2.0.4 on 2018-04-22 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0011_auto_20180422_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='userMoreInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('designation', models.CharField(choices=[(1, 'Teacher'), (2, 'Student')], max_length=1)),
                ('profilephoto', models.FileField(upload_to='upload/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
