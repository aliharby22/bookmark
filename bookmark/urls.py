from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *


app_name = "bookmark"


urlpatterns = [
    # user auth
    path(
        "user/",
        include(
            [
                path("login/", TokenObtainPairView.as_view(), name="login"),
                path(
                    "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
                ),
            ]
        ),
    ),
    # bookmarks
    path(
        "bookmarks/",
        include(
            [
                path("labs/", LabListAPIView.as_view(), name="labs"),
                path("challenges/", ChallengeListAPIView.as_view(), name="challenges"),
                path(
                    "bookmark-item/", BookMarkItemView.as_view(), name="bookmark-item"
                ),
                path(
                    "unbookmark-item/",
                    UnBookMarkItemView.as_view(),
                    name="unbookmark-item",
                ),
                path(
                    "lab-bookmarks/",
                    LabBookmarkListView.as_view(),
                    name="lab-bookmarks",
                ),
                path(
                    "challenge-bookmarks/",
                    ChallengeBookmarkListView.as_view(),
                    name="challenge-bookmarks",
                ),
            ]
        ),
    ),
]
