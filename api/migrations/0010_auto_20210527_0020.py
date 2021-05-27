# Generated by Django 3.2.3 on 2021-05-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20210526_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',), 'verbose_name': 'post', 'verbose_name_plural': 'сообщения'},
        ),
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(help_text='Краткое, уникальное слово, которое будет видно в ссылке на страницу группы (часть URL)', max_length=100, verbose_name='url group'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts_post',
        ),
    ]