from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, status, viewsets
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response

from .filters import PostFilter
from .models import Comment, Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)

User = get_user_model()


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]

    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter

    def perform_create(self, serializer):
        user = User.objects.filter(username=self.request.user)
        if not user.exists():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        group_id = self.request.query_params.get('group', None)
        if group_id is not None:
            return self.queryset.filter(group=group_id)
        return 1


class GroupModelViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentModelViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        get_object_or_404(Post, pk=self.request.data['post'])
        serializer.save(author=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['id'])


class FollowModelViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['user__username', ]

    def perform_create(self, serializer):
        following = self.request.data.get('following')
        user = self.request.user
        if following is None:
            raise ParseError('Bad Request')
        try:
            following = User.objects.get(username=following)
        except User.DoesNotExist:
            raise NotFound('Not Found')
        if (Follow.objects.filter(user=user, following=following)
                or following == user):
            raise ParseError('Bad Request')
        serializer.save(user=user, following=following)

    def get_queryset(self):
        return Follow.objects.filter(following=self.request.user)
