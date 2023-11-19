from rest_framework import serializers
from .models import *


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = "__all__"


class LabBookmarkSerializer(serializers.ModelSerializer):
    lab = LabSerializer(read_only=True)

    class Meta:
        model = LabBookmark
        fields = "__all__"


class ChallengeBookmarkSerializer(serializers.ModelSerializer):
    challenge = ChallengeSerializer(read_only=True)

    class Meta:
        model = ChallengeBookmark
        fields = "__all__"


class BookMarkItemSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    type = serializers.CharField()


class UnBookMarkItemSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()


class LabAndChallengeBookmarkSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    lab = LabBookmarkSerializer(required=False)
    challenge = ChallengeBookmarkSerializer(required=False)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
