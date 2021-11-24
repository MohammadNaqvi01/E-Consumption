from rest_framework import serializers
class RestSerializer(serializers.Serializer):
    timein=serializers.CharField()
    timeout=serializers.CharField()
    appliance=serializers.CharField()
    kwh=serializers.IntegerField()