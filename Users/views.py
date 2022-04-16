from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Users.models import Student, CustomUser
from Users.serializers import RegistrationSerializer, GetUsersInfoSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        if 'is_student' in request.POST:
            student = Student(user=serializer.save(),
                              grade=request.POST.get('grade'))
            student.save()
            return Response('created')
        elif 'is_advisor' in request.POST:
            pass
    else:
        return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    data = {}
    try:
        user = CustomUser.objects.get(phone=request.POST.get('phone'))
        if user.check_password(request.POST.get('password')):
            user.is_active = True
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
        else:
            data['message'] = 'password is incorrect'
    except CustomUser.DoesNotExist:
        data['message'] = 'no user found with this phone'
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    Token.objects.filter(user=user).delete()
    user.is_active = False
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    if user.check_password(request.POST.get('password')):
        user.set_password(request.POST.get('new_password'))
        user.save()
        return Response({'message': 'password changed'})
    else:
        return Response({'message': 'password is incorrect'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_info(request):
    if 'user_id' in request.POST:
        user = CustomUser.objects.get(id=request.POST.get('user_id'))
        serializer = GetUsersInfoSerializer(data=user)
        return Response(serializer.data)
    else:
        user = request.user
        serializer = GetUsersInfoSerializer(user)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_info(request):
    user = request.user
    if 'name' in request.POST:
        user.name = request.POST.get('name')
    if 'username' in request.POST:
        user.username = request.POST.get('username')
    if 'email' in request.POST:
        user.email = request.POST.get('email')
    if 'isvisible' in request.POST:
        user.isvisible = request.POST.get('isvisible')
    if 'grade' in request.POST:
        student = Student.objects.get(user=user)
        student.grade = request.POST.get('grade')
        student.save()
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_account(request):
    if request.user.check_password(request.POST.get('password')):
        request.user.delete()
        return Response({'message': 'account deleted successfully'})
    else:
        return Response({'message': 'password is incorrect'})
