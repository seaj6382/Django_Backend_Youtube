from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


# Create your views here.

# 구독 관련 REST API

# SubscriptionList
# api/v1/subscription
# [GET]: pk = 나 자신. (pk 입력받을 필요X)
# [POST]: 구독하기
class SubscriptionList(APIView):
    
    # 내가 구독하고 있는 유튜버 리스트
    def get(self, request):
        subs = Subscription.objects.filter(subscriber=request.user)
        # objdects -> json
        serializer = SubSerializer(subs, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        user_data = request.data # json -> object (Serializer)
        serializer = SubSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)
    
    

# SubscriptionDetail
# api/v1/subscription/{user_id}
# [GET]: 특정 유저의 구독자 리스트 조회
# [DELETE]: 구독 취소

from .models import Subscription
class SubscriptionDetail(APIView):
    def get(self, request, pk):
        # api/vq/sub/{pk} -> 1번 유저가 구독한 구독자 수가 1이면 OK
        subs = Subscription.objects.filter(subscribed_to=pk)
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data) # 기본값 : 200
    
    # api/v1/sub/{pk}
    def delete(self, request, pk):
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


        # *arg, **kwargs
        # - arg : 위치 기반
        # - kwargs: 키워드 기반
        # 

