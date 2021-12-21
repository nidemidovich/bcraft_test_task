from rest_framework import serializers

from .models import Statistics


class GetStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = [
            'date',
            'views',
            'clicks',
            'cost',
            'cpc',
            'cpm'
        ]


class SendStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'
