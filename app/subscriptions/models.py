from django.db import models
from common.models import CommonModel
from users.models import User

# - User:FK => subscriber (내가 구독한 사람)
# - User:FK => subscribed_to (나를 구독한 사람)

# User:Subscrition => User => 

# Create your models here.

class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')

    # subscriber_set -> subscriptions
    # subscribed_to_set -> subscribers
