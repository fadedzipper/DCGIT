from rest_framework import serializers
from report import models

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'name', 'topic', 'phone', 'email', 'handled']



class ReportListallSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['info']


class ReportAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'name', 'topic', 'phone', 'email', 'handled', 'info']

