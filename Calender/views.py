from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Calender.models import Task
from Calender.serializer import TaskSerializer, GetTaskSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_task(request):
    serializer = TaskSerializer(data=request.data,
                                context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_task(request):
    tasks = Task.objects.filter(date=request.POST.get('date'))
    serializer = GetTaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_task(request):
    task = Task.objects.get(id=request.POST.get('task_id'))
    if task.user == request.user:
        task.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)

