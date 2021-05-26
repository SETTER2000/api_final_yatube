# Generated by Django 3.2.3 on 2021-05-25 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Придумайте краткое и ёмкое название для группы сообщений', max_length=200, verbose_name='название группы')),
                ('slug', models.SlugField(help_text='Краткое, уникальное слово, которое будет видно в ссылке на страницу группы (часть URL)', max_length=100, unique=True, verbose_name='url group')),
                ('description', models.TextField(help_text='Опишите группу так, чтобы пользователь мог легко  определиться с выбором группы для сообщения.', verbose_name='описание')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'Группа',
                'db_table': 'posts_group',
            },
        ),
    ]
