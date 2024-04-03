from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.

class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법

    user = models.ForeignKey(User, on_delete=models.CASCADE) # 운영의 문제
    

    # User:Video
        # => User : Video, Video, Video, Video, Video => O
        # => Video : User, User, User (유튜버 3명이 찍은 영상) => X
