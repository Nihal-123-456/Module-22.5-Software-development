# Generated by Django 4.2.4 on 2023-12-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_alter_transactionmodel_transaction_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_bankrupt', models.BooleanField(default=False)),
            ],
        ),
    ]