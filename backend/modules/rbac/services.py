from .models import Role,Permission
from django.db import transaction


@transaction.atomic
def create_role(name, description="", is_active=True):
    return Role.objects.create(
        name=name,
        description=description,
        is_active=is_active,
    )


@transaction.atomic
def update_role(role, name=None, description=None, is_active=None):
    if name is not None:
        role.name = name

    if description is not None:
        role.description = description

    if is_active is not None:
        role.is_active = is_active

    role.save()

    return role


@transaction.atomic
def delete_role(role):
    role.is_active = False
    role.save(update_fields=["is_active"])

    return role


@transaction.atomic
def create_permission(name, codename, description="", is_active=True):
    return Permission.objects.create(
        name=name,
        codename=codename,
        description=description,
        is_active=is_active,
    )


@transaction.atomic
def assign_permissions_to_role(role, permissions):
    role.permissions.add(*permissions)
    return role


@transaction.atomic
def remove_permissions_from_role(role, permissions):
    role.permissions.remove(*permissions)
    return role


@transaction.atomic
def assign_roles_to_user(user, role):
    user.roles.add(*role)
    return user


@transaction.atomic
def remove_roles_from_user(user, role):
    user.roles.remove(*role)
    return user
