from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Lessons.models import Lesson
from Lessons.seializers import LessonsSerializer
from Users.models import Student


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_lessons(request):
    user = request.user
    if user.is_student:
        student = Student.objects.get(user=user)
        lessons = Lesson.objects.filter(grade=student.grade)
        serializer = LessonsSerializer(lessons, many=True)
        return Response(serializer.data)
    elif 'grade' in request.POST:
        lessons = Lesson.objects.filter(grade=request.POST.get('grade'))
        serializer = LessonsSerializer(lessons, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



