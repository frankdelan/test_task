from django.db.models import Q
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from .models import Access, Product, Lesson
from .serializers import AccessSerializer, ProductSerializer, LessonSerializer


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
        prod = request.data.get('product')
        user = request.data.get('user')
        try:
            Access.objects.get(Q(product__name=prod) & Q(user__username=user))
        except:
            return Response({'status': 'error',
                             'data': None,
                             'detail': 'User has no access or user does not exist.'})

        lessons = Lesson.objects.filter(product__name=prod)
        return Response({'status': 'success',
                         'data': LessonSerializer(lessons, many=True).data,
                         'detail': None})
