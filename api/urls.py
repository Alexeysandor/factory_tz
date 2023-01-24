from django.urls import path

from api.views import AddCreatedRobot


urlpatterns = [
    path('add_robot', AddCreatedRobot.as_view()),
]
