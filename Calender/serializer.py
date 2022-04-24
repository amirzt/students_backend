from rest_framework import serializers

from Calender.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user', 'date']

    def save(self, **kwargs):
        task = Task(user=self.context['request'].user,
                    date=self.validated_data['date'])
        if 'description' in kwargs:
            task.description = kwargs.get('description')
        if 'send_notification' in kwargs:
            task.send_notification = kwargs.get('send_notification')
        task.save()
        return task


class GetTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['user', 'date', 'description', 'id']
