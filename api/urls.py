from django.urls import include, re_path
from rest_framework import routers

from . import views as vs

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', vs.PostModelViewSet, basename='post')
router_v1.register(r'group', vs.GroupModelViewSet, basename='group')
router_v1.register(r'follow', vs.FollowModelViewSet, basename='follow')
router_v1.register(r'posts/(?P<id>[0-9]+)/comments', vs.CommentModelViewSet,
                   basename='comment')
urlpatterns = [
    re_path(r'^v1/', include(router_v1.urls)),
]
