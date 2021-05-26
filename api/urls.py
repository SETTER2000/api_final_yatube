from django.urls import include, re_path
from rest_framework import routers

from . import views as vs

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', vs.PostModelViewSet)
router_v1.register(r'group', vs.GroupModelViewSet)
router_v1.register(r'follow', vs.FollowModelViewSet)
router_v1.register(r'posts/(?P<id>[0-9]+)/comments', vs.CommentModelViewSet)
urlpatterns = [
    re_path(r'^v1/', include(router_v1.urls)),
]
