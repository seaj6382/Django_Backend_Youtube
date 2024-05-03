from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):

     # Video:User => Video(FK) -> User
    user = UserSerializer(read_only=True) # Video(FK)

    # Video:Comment => Video -> Cooment(FK)
        # Reverse Accessor
        # 부모가 자녀를 찾을때 = _set으로 부모에 속한 자녀들을 모두 찾을 수 있다.


    class Meta:
        model = Video
        fields = '__all__'
        # depth = 1

from reactions.models import Reaction
class VideoDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True) # Video(FK)
    comment_set = CommentSerializer(many=True, read_only=True)

    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'
        # depth = 1

    def get_reactions(self, video):
        return Reaction.get_video_reaction(video) # 비디오 줄게 -> 리액션 내놔.

