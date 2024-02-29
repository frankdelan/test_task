from .models import UserGroup, Product, Access, Lesson
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers


class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = "__all__"


class AccessSerializer(serializers.Serializer):
    product = serializers.CharField()
    user = serializers.CharField()

    def create(self, validated_data):
        try:
            product_name = Product.objects.get(name=validated_data.get('product'))
            username = User.objects.get(username=validated_data.get('user'))
        except:
            return {'status': "error",
                    'data': None,
                    'detail': "User or product does not exist."}

        low_group = UserGroup.objects.filter(product_id=product_name).annotate(num_students=Count('students')).order_by(
            'num_students').first()

        if low_group.min_user_count < low_group.num_students < low_group.max_user_count:
            low_group.students.add(username)
            return {'status': "success",
                    'data': UserGroupSerializer(low_group).data,
                    'detail': f"User added in the group {low_group.name}"}
        else:
            raise {'status': "error",
                   'data': None,
                   'detail': "There are no places"}


class ProductSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(product=obj).count()

    class Meta:
        model = Product
        fields = ('id', 'name', 'date', 'start_time', 'price', 'author', 'lesson_count')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
