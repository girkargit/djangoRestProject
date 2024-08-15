from rest_framework import serializers
from .models import *

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name', 'id']

class PeopleSerializer(serializers.ModelSerializer):

    color = ColorSerializer()
    country = serializers.SerializerMetaclass()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1

    def get_country(self, obj):
        return "India"

    def validate(self, data):
        if data["name"]:
            for i in data["name"]:
                if i in "!@#$%^&*()":
                    raise serializers.ValidationError("Name can not contain special character.")
        elif data["age"] < 18:
            raise serializers.ValidationError("Age should greater than 18.")
        return data