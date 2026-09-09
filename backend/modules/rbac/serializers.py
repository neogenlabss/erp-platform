from dataclasses import fields
from rest_framework import serializers
from .models import Role,Permissions

class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permissions

        fields=[
            "id",
            "name",
            "codename",
            "description",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields=["id","created_at","updated_at"]

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role

        fields=[
            "id",
            "name",
            "description",
            "permissions",
            "is_active",
            "created_at",
            "updated_at",
        ]
        
        read_only_fields=["id","created_at","updated_at"]