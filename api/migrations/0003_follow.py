# Generated by Django 3.2.3 on 2021-05-26 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(help_text='Пользователь, на которого подписываются.', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
                ('user', models.ForeignKey(help_text='Пользователь, который подписывается.', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='подписчик')),
            ],
            options={
                'verbose_name': 'follow',
                'verbose_name_plural': 'Подписки',
                'db_table': 'follow_author',
                'ordering': ('-author',),
            },
        ),
    ]
