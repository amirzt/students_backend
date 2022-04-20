
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Friendship.models import SearchAccount, Request
from Friendship.serializers import SearchAccountSerializer, SendRequestSerializer, GetRequestSerializer
from Users.models import Student
from Users.serializers import GetStudentSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_account(request):
    serializer = SearchAccountSerializer(data=request.data,
                                         context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    try:
        account = SearchAccount.objects.get(user=request.user)
        account.delete()
        return Response(status=status.HTTP_200_OK)
    except SearchAccount.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_match(request):
    search_account = SearchAccount.objects.get(user=request.user)
    matches = Student.objects.filter(grade=search_account.grade,
                                     gender=search_account.gender)
    serializer = GetStudentSerializer(matches, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_request(request):
    serializer = SendRequestSerializer(data=request.data,
                                       context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_my_requests(request):
    requests = Request.objects.filter(receiver=request.user,
                                      state=2)
    serializer = GetRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_sent_requests(request):
    requests = Request.objects.filter(sender=request.user)
    serializer = GetRequestSerializer(requests, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def interact_request(request):
    try:
        data = Request.objects.get(id=request.POST.get('request_id'))
        if 'status' in request:
            data.state = request.POST.get('state')
            data.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except Request.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_request(request):
    data = Request.objects.get(id=request.POST.get('request_id'))
    if data.sender == request.user:
        data.delete()
        return Response({'message': 'deleted'})
    else:
        return Response({'message': 'you only can delete your own request'})


