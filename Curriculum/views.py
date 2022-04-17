from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Curriculum.models import CurriculumItem
from Curriculum.serializers import GetCurriculumSerializer
from Lessons.seializers import AddScheduleItemSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_curriculum(request):
    schedule_serializer = AddScheduleItemSerializer(data=request.POST.get('schedule'))

    if schedule_serializer.is_valid():
        schedule = schedule_serializer.save()
        curriculum = CurriculumItem(schedule=schedule,
                                    day=request.POST.get('day'),
                                    week=request.POST.get('week'),
                                    user=request.user)
        curriculum.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(schedule_serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_week(request):
    curriculum = CurriculumItem.objects.filter(user=request.user,
                                               week=request.POST.get('week'))
    serializers = GetCurriculumSerializer(curriculum)
    return Response(serializers.data)
