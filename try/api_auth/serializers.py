from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'password', 'email', 'date_created', 'last_login_date', 'active')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        return User.objects.create_user(**data)
