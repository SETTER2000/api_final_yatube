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
        # unique=True,
        blank=True,
        null=True,
        max_length=100,
        verbose_name='url group',
        help_text='Краткое, уникальное слово, которое будет '
                  'видно в ссылке на страницу группы (часть URL)')
    description = models.TextField(
        'описание',
        blank=True,
        null=True,
        help_text='Опишите группу так, чтобы пользователь мог легко  '
                  'определиться с выбором группы для сообщения.')

    class Meta:
        db_table = 'posts_group'
        verbose_name = 'group'
        verbose_name_plural = 'Группа'


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    group = models.ForeignKey(
        'Group',
        models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='группа',
        help_text='Группа сообщений.',
        related_name='group_posts')

    class Meta:
        db_table = 'posts_post'
        ordering = ('-pub_date',)
        verbose_name = 'post'
        verbose_name_plural = 'сообщения'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='Пользователь, на которого подписываются.',
        related_name='following')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        verbose_name='подписчик',
        help_text='Кто подписался (Подписчик)',
        related_name='follower')


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique user_following',
            )
        ]
