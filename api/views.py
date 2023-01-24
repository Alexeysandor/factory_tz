from rest_framework.generics import CreateAPIView

from .serializers import Robot_serializer


class AddCreatedRobot(CreateAPIView):
    serializer_class = Robot_serializer
