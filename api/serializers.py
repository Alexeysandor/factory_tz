from rest_framework.serializers import ModelSerializer, ValidationError
from robots.models import Robots
from orders.models import Order


class Robot_serializer(ModelSerializer):
    # валидатор для модели робота.
    class Meta:
        model = Robots
        fields = ('model', 'version', 'created')

    def create(self, validated_data):
        # Поскольку в ТЗ передаются модель и версия, я решил,
        # что следует генерировать значение серии
        # непосредственно в сериализаторе
        serial = f"{validated_data['model']}-{validated_data['version']}"
        # После этого мы передаёт значение серии в данные для сохранения
        validated_data['serial'] = serial
        return Robots.objects.create(**validated_data)


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_in_db = Order.objects.filter(
            robot_serial=validated_data['robot_serial'],
            customer_id=validated_data['customer'],
            waiting_list=True)
        if order_in_db:
            raise ValidationError(
                'Вы уже оформляли заказ на эту серию робота, \n'
                'но его до сих пор нет в наличии. \n'
                'Как только он появится, мы отправим вам письмо')
        return Order.objects.create(**validated_data)
