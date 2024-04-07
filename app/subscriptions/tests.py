from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse

# Create your tests here.
class SubscriptionTestCase(APITestCase):
    # 테스트 코드 실행 시 가장 먼저 실행되는 함수
    # - 데이터 생성
    #  - 2명의 유저 데이터 생성, 1명의 유저 로그인
    def setUp(self):
        self.user1 = User.objects.create_user(email='test1', password='pw1231')
        self.user2 = User.objects.create_user(email='test', password='pw1231')

        self.client.login(email='test1', password='pw1231')

    # 구독 버튼 테스트
    def test_sub_list_post(self):
        def test_sub_list_post(self):
            url = reverse('sub-list')
            data = {
                'subscriber': self.user1.pk ,
                'subscribed_to': self.user2.pk
            }

            res = self.client.post(url, data)
            self.assertEqual(res.status_code, 201) # 201: CREATE
            from .models import Subscription
            self.assertEqual(Subscription.objects.get().subscribed_to, self.user2)
            self.assertEqual(Subscription.objects.count(), 1)

    # 특정 유저의 구독자 리스트
    def test_sub_detail_get(self):
        pass

    # 구독취소 
    def test_sub_detail_delete(self):
        pass