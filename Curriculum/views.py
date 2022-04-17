import logging

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
    schedule_serializer = AddScheduleItemSerializer(data=request.data)

    if schedule_serializer.is_valid():
        schedule = schedule_serializer.save()
        curriculum = CurriculumItem(scheduleItem=schedule,
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
    serializers = GetCurriculumSerializer(curriculum, many=True)
    return Response(serializers.data)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_total_week(request):
#     response = {}
#     curriculum = CurriculumItem.objects.filter(user=request.user,
#                                                week=request.POST.get('week')).order_by('day')
#     total_time = 0
#     day_time = 0
#     for index, curriculum in enumerate(curriculum):
#         total_time = total_time+curriculum.scheduleItem.time
#         if curriculum.day != curriculum[index+1].day:
#             response[curriculum.day] = day_time
#             day_time = 0
#         else:
#             day_time += curriculum.scheduleItem.time
#
#     response['total_time'] = total_time
#
#     return Response(response)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request):
    try:
        curriculum = CurriculumItem.objects.get(id=request.POST.get('curriculum'))
        if request.user == curriculum.user:
            curriculum.scheduleItem.delete()
            curriculum.delete()
            return Response({'message': 'deleted'})
        else:
            return Response({'message': 'you only can delete your own curriculum'})
    except CurriculumItem.DoesNotExist:
        return Response({'message': 'item does not exist'})


