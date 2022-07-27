import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from atwdm.models import Tool, User
from atwdm.producer import publish
from atwdm.serializers import ToolSerializer


class ToolViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving tools.
    """
    def list(self, request):
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        tool = Tool.objects.get(id=pk)
        serializer = ToolSerializer(tool)
        return Response(serializer.data)

    def create(self, request):
        serializer = ToolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(method='tool_created', body=serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        tool = Tool.objects.get(id=pk)
        serializer = ToolSerializer(instance=tool, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(method='tool_updated', body=serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        tool = Tool.objects.get(id=pk)
        tool.delete()
        publish(method='tool_deleted', body=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
