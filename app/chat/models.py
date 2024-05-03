from django.db import models
from common.models import CommonModel

# Create your models here.

# ChatRoom 모델의 분리했을 때의 이점
# - 관리가 용의
# - 확장성(채팅방: 오픈, 업무-비밀방)
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)

class ChatMessage(CommonModel):
    # 정보통신법 3개월 채팅 보관
    # SET_NULL - sender null rkqtdmfh enrpTeksms Emt, 1번 -> 계정삭제 -> null
    sender = models.ForeignKey('users.User',  on_delete=models.SET_NULL, null=True) # 알수없음
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

# User:Msg(FK)
    # - User:Msg => 1:N (O)
    # - Msg: User => 1:N (X)

# Room:Msg
    # - Room:Msg => 1:N (O)
    # - Msg:Room => 1:N (X)