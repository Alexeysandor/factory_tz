from rest_framework.generics import CreateAPIView

from robots.models import Robots
from .serializers import Robot_serializer, OrderSerializer


class AddCreatedRobot(CreateAPIView):
    serializer_class = Robot_serializer


class CreateOrder(CreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        robot_serial = self.request.data.get('robot_serial')
        robot = Robots.objects.filter(serial=robot_serial).first()
        if robot:
            serializer.save()
        else:
            serializer.validated_data['waiting_list'] = True
            serializer.save()
