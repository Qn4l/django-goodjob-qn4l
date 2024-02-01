# Generated by Django 5.0.1 on 2024-01-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0004_alter_subscribe_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='option',
            field=models.CharField(choices=[('W', 'Weekly'), ('M', 'Monthly'), ('Y', 'Yearly')], default='M', max_length=1),
        ),
    ]
