from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404


class LabListAPIView(generics.ListAPIView):
    """View to list all labs"""

    queryset = Lab.objects.all()
    serializer_class = LabSerializer


class ChallengeListAPIView(generics.ListAPIView):
    """View to list all challenges"""

    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer


class BookMarkItemView(generics.GenericAPIView):
    """
    bookmark lab/challenge
    """

    serializer_class = BookMarkItemSerializer

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uuid = serializer.validated_data["uuid"]
        type = serializer.validated_data["type"]
        if type == "Lab":
            lab = get_object_or_404(Lab, uuid=uuid)
            LabBookmark.objects.create(lab=lab, user=request.user)
            return Response("Lab Bookmarked!", status=status.HTTP_200_OK)
        elif type == "Challenge":
            challenge = get_object_or_404(Challenge, uuid=uuid)
            ChallengeBookmark.objects.create(challenge=challenge, user=request.user)
            return Response("Challenge Bookmarked!", status=status.HTTP_200_OK)
        return Response("Wrong Item", status=status.HTTP_400_BAD_REQUEST)


class UnBookMarkItemView(generics.GenericAPIView):
    """
    unbookmark lab/challenge
    """

    serializer_class = UnBookMarkItemSerializer

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        uuid = serializer.validated_data["uuid"]
        try:
            lab_bookmark = LabBookmark.objects.get(uuid=uuid)
            lab_bookmark.delete()
            return Response("Deleted!", status=status.HTTP_200_OK)
        except LabBookmark.DoesNotExist:
            challenge_bookmark = get_object_or_404(ChallengeBookmark, uuid=uuid)
            challenge_bookmark.delete()
            return Response("Deleted!", status=status.HTTP_200_OK)
        except:
            return Response("Not Found!", status=status.HTTP_404_NOT_FOUND)


class LabBookmarkListView(generics.ListAPIView):
    serializer_class = LabBookmarkSerializer
    queryset = LabBookmark.objects.all()

    def get_queryset(self):
        user = self.request.user
        lab_query = LabBookmark.objects.filter(user=user).select_related("user", "lab")
        return lab_query


class ChallengeBookmarkListView(generics.ListAPIView):
    serializer_class = ChallengeBookmarkSerializer
    queryset = ChallengeBookmark.objects.all()

    def get_queryset(self):
        user = self.request.user
        challenge_query = ChallengeBookmark.objects.filter(user=user).select_related(
            "user", "challenge"
        )
        return challenge_query
