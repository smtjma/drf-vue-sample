from django.shortcuts import render
from rest_framework import viewsets
from userinfo.models import User_id_table
from .serializers import User_id_tableSerializer

# Create your views here.
class User_id_tableViewSet(viewsets.ModelViewSet):
    queryset = User_id_table.objects.all()
    serializer_class = User_id_tableSerializer
    