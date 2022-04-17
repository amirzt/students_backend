from rest_framework import serializers

from Lessons.models import Lesson, ScheduleItem


class LessonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ['title', 'grade', 'types', 'icon']


class AddScheduleItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ScheduleItem
        fields = ['lesson', 'time']

    def save(self, **kwargs):
        schedule = ScheduleItem(lesson=self.validated_data['lesson'],
                                time=self.validated_data['time'])
        schedule.save()
        return schedule
