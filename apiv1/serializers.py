from rest_framework import serializers
from userinfo.models import User_id_table

class User_id_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_id_table
        fields = ['id', 'name', 'created_at']
        