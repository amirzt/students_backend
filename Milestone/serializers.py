from rest_framework import serializers

from Milestone.models import Milestone


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        models = Milestone
        fields = ['title', 'date']

    def save(self, **kwargs):
        milestone = Milestone(user=self.context['request'].user,
                              title=self.validated_data['title'],
                              date=self.validated_data['date'])
        if 'description' in kwargs:
            milestone.description = kwargs.get('description')

        milestone.save()
        return milestone


class GetMilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        models = Milestone
        fields = ['title', 'date', 'description', 'state']
