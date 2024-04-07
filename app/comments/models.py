from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

# Create your models here.
class Comment(CommonModel):
    conent = models.TextField()
    like = models.PositiveBigIntegerField(default=0)
    dislike = models.PositiveBigIntegerField(default=0)

    # User: Comment = 1:N

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Video:Comment = 1:N

    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    # 법(law) -> 채팅 데이터 3개월

    # docker-compose run --rm app sh -c 'python manage.py makemigrations'
    # docker-compose run --rm app sh -c 'python manage.py migrate'