from rest_framework import serializers
from xiaopingguo.models import User_info
from django.contrib.auth.models import User


class User_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = ['name', 'phone', 'address', 'add_more', 'surplus_apple', 'surplus_apple', 'score']
