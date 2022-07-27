from django.urls import path
from atwdm.views import ToolViewSet, UserAPIView

urlpatterns = [
    path('tools', ToolViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('tools/<int:pk>', ToolViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
    path('user', UserAPIView.as_view()),
]
