from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from . import api_serializers


class CartView(APIView):
    def get(self, request, format=None):
        cart = request.get_cart()
        data = api_serializers.CartSerializer(cart).data
        return Response(data)


class CartItemView(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        cart = self.request.get_cart()
        return cart.items.get_subclass(id=self.kwargs['id'])

    def get_serializer(self, instance, *args, **kwargs):
        ser_class = api_serializers.registry.get_serializer_class(instance)
        return ser_class(instance, cart=self.request.get_cart(),
                         *args, **kwargs)


class AddToCartView(CreateAPIView):
    def get_serializer(self, data, *args, **kwargs):
        ser_class = api_serializers.registry[data['type']]
        return ser_class(data=data['data'], cart=self.request.get_cart(),
                         *args, **kwargs)
