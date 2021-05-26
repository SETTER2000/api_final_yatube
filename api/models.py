from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Сообщество."""
    title = models.CharField(
        'название группы',
        max_length=200,
        help_text='Придумайте краткое и ёмкое название для группы сообщений')
    slug = models.SlugField(
        unique=True,
        max_length=100,
        verbose_name='url group',
        help_text='Краткое, уникальное слово, которое будет '
                  'видно в ссылке на страницу группы (часть URL)')
    description = models.TextField(
        'описание',
        help_text='Опишите группу так, чтобы пользователь мог легко  '
                  'определиться с выбором группы для сообщения.')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts_group'
        verbose_name = 'group'
        verbose_name_plural = 'Группа'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='подписчик',
        help_text='Пользователь, который подписывается.',
        related_name='follower')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='Пользователь, на которого подписываются.',
        related_name='following')

    class Meta:
        db_table = 'follow_author'
        verbose_name = 'follow'
        ordering = ('-author',)
        verbose_name_plural = 'Подписки'