import rest_framework.generics as generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Statistics
from .serializers import GetStatisticsSerializer, SendStatisticsSerializer


class GetStatisticsView(generics.ListAPIView):
    serializer_class = GetStatisticsSerializer
    queryset = Statistics.objects.order_by('date')


class GetStatisticsForPeriodView(generics.ListAPIView):
    serializer_class = GetStatisticsSerializer

    def get_queryset(self):
        start_date = self.kwargs.get('start_date')
        end_date = self.kwargs.get('end_date')
        sort_column = self.request.query_params.get('sort_by')
        if sort_column in [f.name for f in Statistics._meta.get_fields()]:
            queryset = Statistics.objects.filter(
                date__gte=start_date,
                date__lte=end_date
            ).order_by(sort_column)
            return queryset

        queryset = Statistics.objects.filter(
            date__gte=start_date, date__lte=end_date
        ).order_by('date')
        return queryset


class SendStatisticsView(generics.CreateAPIView):
    serializer_class = SendStatisticsSerializer


class DeleteStatisticsView(APIView):
    def delete(self, request):
        Statistics.objects.all().delete()
        return Response({'result': 'Success'})
