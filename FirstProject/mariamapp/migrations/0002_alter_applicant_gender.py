# Generated by Django 4.0.3 on 2022-04-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mariamapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='male', max_length=6),
        ),
    ]
