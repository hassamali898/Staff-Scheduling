from webbrowser import get
from rest_framework import serializers
from schedule.models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
    
    def create(self, validated_data):
        return Schedule.objects.create(**validated_data)
        
    