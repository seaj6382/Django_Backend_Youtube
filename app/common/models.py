from django.db import models

# Create your models here.
class CommonModel(models.Model):

    created_at = models.DateField(auto_now_add=True) # 생성된 시간 (고정)
    
    # 데이터가 업데이트된 시간 (업데이트 할 때 마다 계속 시간이 변경)
    updated_at = models.DateTimeFiedld(auto_now=True)

    class Meta:
        abstract = True # DB에 테이블을 추가하지 마시오.