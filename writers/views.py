from rest_framework import viewsets
from .models import Writer
from .serializers import WriterSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
