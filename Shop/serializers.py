from rest_framework import serializers

from Shop.models import Plan, Order


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['title', 'detail', 'period', 'price', 'id']


class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['plan']

    def save(self, **kwargs):
        order = Order(plan_id=self.validated_data['plan'],
                      user=self.context['request'].user)
        order.save()
        return order


class GetOrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['plan', 'created_time', 'modified_time', 'state', 'tracking_code']
