from dataclasses import fields
from rest_framework import serializers
from .models import Role,Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Permission

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