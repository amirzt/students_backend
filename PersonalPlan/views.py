from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Lessons.seializers import AddScheduleItemSerializer
from PersonalPlan.models import PersonalPlan
from PersonalPlan.serializers import GetPersonalPlanSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_personal_plan(request):
    schedule_serializer = AddScheduleItemSerializer(data=request.data)

    if schedule_serializer.is_valid():
        schedule = schedule_serializer.save()
        plan = PersonalPlan(scheduleItem=schedule,
                            date=request.POST.get('date'),
                            user=request.user)
        plan.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(schedule_serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_week(request):
    plans = PersonalPlan.objects.filter(user=request.user)
    serializers = GetPersonalPlanSerializer(plans, many=True)
    return Response(serializers.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete(request):

    try:
        plan = PersonalPlan.objects.get(id=request.POST.get('curriculum'))
        if request.user == plan.user:
            plan.scheduleItem.delete()
            plan.delete()
            return Response({'message': 'deleted'})
        else:
            return Response({'message': 'you only can delete your own curriculum'})
    except PersonalPlan.DoesNotExist:
        return Response({'message': 'item does not exist'})


