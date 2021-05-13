from rest_framework import serializers

from .models import Dealers, Cars


class DealersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dealers
        fields = ('id', 'title', 'location', 'year',)


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'brand', 'car_model', 'year_of_release', 'price', 'dealer',)
