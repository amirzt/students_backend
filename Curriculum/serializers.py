from rest_framework import serializers

from Curriculum.models import CurriculumItem


class GetCurriculumSerializer(serializers.ModelSerializer):

    class Meta:
        model = CurriculumItem
        fields = ['scheduleItem', 'day', 'week']
