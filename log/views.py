from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SysLog
from .serializers import LogSerializer
from rest_framework.pagination import  PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.
from permission import permissions


class SelfPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class SyslogView(ModelViewSet):

    permission_classes = (permissions.ModelPermission,)
    serializer_class = LogSerializer
    pagination_class = SelfPagination
    queryset = SysLog.objects.all().order_by("log_id")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ('log_type','log_content','log_user','log_dotype')