# Generated by Django 3.2.3 on 2021-05-26 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210526_1651'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='follow',
            table='follow_following',
        ),
    ]
