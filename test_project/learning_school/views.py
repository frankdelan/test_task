from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Access, Product
from .serializers import AccessSerializer, ProductSerializer, LessonAccessSerializer


class AccessAPIView(generics.CreateAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.validated_data)
        return Response(data)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonAPIView(APIView):
    def post(self, request):
        serializer = LessonAccessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        return Response(data)
