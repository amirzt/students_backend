from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from Shop.models import Plan, Order
from Shop.serializers import PlanSerializer, CreateOrderSerializer, GetOrdersSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def get_plans(request):
    plans = Plan.objects.filter(available=True)
    serializer = PlanSerializer(plans, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def order(request):
    serializer = CreateOrderSerializer(data=request.data,
                                       context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders = Order.objects.filter(user=request.user)
    serializer = GetOrdersSerializer(orders, many=True)
    return Response(serializer.data)
