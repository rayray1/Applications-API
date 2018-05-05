from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser

from applications import models
from . import serializers


class ListApps(generics.ListCreateAPIView):
    parser_classes = (MultiPartParser, FormParser)
    queryset = models.Applist.objects.all()
    serializer_class = serializers.ApplistSerializer
