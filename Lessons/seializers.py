from rest_framework import serializers

from Lessons.models import Lesson


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title', 'grade', 'types', 'icon']
