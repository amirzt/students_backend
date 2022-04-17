from rest_framework import serializers

from PersonalPlan.models import PersonalPlan


class GetPersonalPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = PersonalPlan
        fields = ['scheduleItem', 'day', 'week']
