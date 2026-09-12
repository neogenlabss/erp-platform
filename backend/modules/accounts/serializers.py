from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "roles",
            "is_active",
            "is_staff",
            "date_joined",
        )
        read_only_fields = (
            "id",
            "date_joined",
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "first_name",
            "last_name",
            "roles",
        )

    def create(self, validated_data):
        from .services import UserService

        return UserService.create_user(**validated_data)