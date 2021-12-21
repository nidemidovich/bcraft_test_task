import rest_framework.generics as generics

from .models import Statistics
from .serializers import GetStatisticsSerializer, SendStatisticsSerializer


class GetStatisticsView(generics.ListAPIView):
    serializer_class = GetStatisticsSerializer

    def get_queryset(self):
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')
        queryset = Statistics.objects.filter(date__gte=start_date, date__lte=end_date)
        return queryset


class SendStatisticsView(generics.CreateAPIView):
    serializer_class = SendStatisticsSerializer
