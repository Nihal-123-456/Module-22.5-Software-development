# Generated by Django 4.2.4 on 2023-12-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_useraccount_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]