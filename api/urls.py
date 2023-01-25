from django.urls import path

from api.views import AddCreatedRobot, CreateOrder


urlpatterns = [
    path('add_robot', AddCreatedRobot.as_view()),
    path('create_order', CreateOrder.as_view()),
]
