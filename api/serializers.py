from rest_framework import serializers
from applications import models


class ApplistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Applist
        fields = ('application', 'package_name', 'package_version_code',)
