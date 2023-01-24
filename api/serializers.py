from rest_framework.serializers import ModelSerializer

from robots.models import Order


class Robot_serializer(ModelSerializer):
    # валидатор для модели робота.
    class Meta:
        model = Order
        fields = ('model', 'version', 'created')

    def create(self, validated_data):
        # Поскольку в ТЗ передаются модель и версия, я решил,
        # что следует генерировать значение серии
        # непосредственно в сериализаторе
        serial = f"{validated_data['model']}-{validated_data['version']}"
        # После этого мы передаёт значение серии в данные для сохранения
        validated_data['serial'] = serial
        return Order.objects.create(**validated_data)
