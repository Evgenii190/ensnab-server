from rest_framework import serializers
from.models import Service, ServiceContent, ServiceSlider, –°ooperation

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ServiceContentSerializer(serializers.ModelSerializer):
    service = serializers.CharField(source='category')
    class Meta:
        model = ServiceContent
        fields = '__all__'

class ServiceSliderSerializer(serializers.ModelSerializer):
    serviceSlug = serializers.CharField(source='category.slug')

    class Meta:
        model = ServiceSlider
        fields = '__all__'

class –°ooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = –°ooperation
        fields = '__all__'