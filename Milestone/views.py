# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Milestone.models import Milestone
from Milestone.serializers import MilestoneSerializer, GetMilestoneSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_milestone(request):
    serializer = MilestoneSerializer(data=request.data,
                                     context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_milestone(request):
    if 'date' in request.POST:
        milestones = Milestone.objects.filter(user=request.user,
                                              date=request.POST.get('date'))
    else:
        milestones = Milestone.objects.filter(user=request.user)
    serializer = GetMilestoneSerializer(milestones, many=True)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_milestone(request):
    milestone = Milestone.objects.get(id=request.POST.get('milestone_id'))
    if milestone.user == request.user:
        milestone.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
