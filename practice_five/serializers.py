from rest_framework import serializers
from .models import *
import re

"""Задание 1 Сериалайзер для модели Category
Создайте сериалайзер для модели Category:
● Позволяет получать, создавать и обновлять записи категории."""


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


"""Задание 2 Сериалайзер для модели Supplier
Создайте сериалайзер для модели Supplier:
● Позволяет получать, создавать и обновлять записи поставщика"""


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


"""Задание 3.1 Сериалайзер для получения данных
Создайте сериалайзер для модели Product:
● Позволяет получать данные продукта.
● Включает связанные объекты Category и Supplier в виде вложенных
сериалайзеров."""


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


"""Задание 3.2 Сериалайзер для создания и обновления данных
Создайте сериалайзер для модели Product:
● Позволяет создавать и обновлять записи продукта.
● Использует первичные ключи для полей category и supplier."""


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


"""Задание 4.1 Сериалайзер для получения данных
Создайте сериалайзер для модели ProductDetail:
● Позволяет получать данные деталей продукта.
● Включает связанные объекты Product в виде вложенного сериалайзера."""


class ProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductDetail
        fields = '__all__'


"""Задание 4.2 Сериалайзер для создания и обновления данных
Создайте сериалайзер для модели ProductDetail:
● Позволяет создавать и обновлять записи деталей продукта.
● Использует первичный ключ для поля product"""


class ProductDetailCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = '__all__'


"""Задание 5 Сериалайзер для модели Address
Создайте сериалайзер для модели Address:
● Позволяет получать, создавать и обновлять записи адреса"""


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


"""Задание 6.1 Сериалайзер для получения данных
Создайте сериалайзер для модели Customer:
● Позволяет получать данные клиента.
● Включает связанные объекты Address в виде вложенного сериалайзера.
● Поля date_joined, deleted и deleted_at не должны быть доступны для создания
и изменения."""


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['date_joined', 'deleted', 'deleted_at']


"""Задание 6.2 Сериалайзер для создания и обновления данных
Создайте сериалайзер для модели Customer:
● Позволяет создавать и обновлять записи клиента.
● Использует первичный ключ для поля address.
● Поля date_joined, deleted и deleted_at не должны быть доступны для создания
и изменения."""


class CustomerCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

    """Задание 6.3 Валидация номера телефона
    Создайте метод валидации для поля phone_number, который:
    ● убедится, что номер телефона состоит из 10՞15 цифр и не содержит букв или
    специальных символов"""

    def validate_phone_number(self, value):
        if not re.match(r'^\d{10,15}$', value):
            raise serializers.ValidationError('Номер телефона должен содержать от 10 до 15 цифр.')
        return value


"""Задание 7.1 Сериалайзер для получения данных
Создайте сериалайзер для модели Order:
● Позволяет получать данные заказа.
● Включает связанные объекты Customer в виде вложенного сериалайзера.
● Поле order_date не должно быть доступным для создания и изменения."""


class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']


"""Задание 7.2 Сериалайзер для создания и обновления данных
Создайте сериалайзер для модели Order:
● Позволяет создавать и обновлять записи заказа.
● Использует первичный ключ для поля customer.
● Поле order_date не должно быть доступным для создания и изменения."""


class OrderCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['order_date']


"""Задание 8.1 Сериалайзер для получения данных
Создайте сериалайзер для модели OrderItem:
● Позволяет получать данные элемента заказа.
● Включает связанные объекты Product и Order в виде вложенных
сериалайзеров."""


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


"""Задание 8.2 Сериалайзер для создания и обновления данных
Создайте сериалайзер для модели OrderItem:
● Позволяет создавать и обновлять записи элемента заказа.
● Использует первичные ключи для полей order и product"""


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

    """Задание 8.3 Валидация количества товара
    Создайте метод валидации для поля quantity, который:
    ● убедится, что количество товара не больше тысячи."""

    def validate_quantity(self, value):
        if value > 1000:
            raise serializers.ValidationError('Количество товара должно быть не больше тысячи.')
        return value


