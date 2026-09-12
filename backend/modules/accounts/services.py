from django.db import transaction

from .models import User


class UserService:

    @staticmethod
    @transaction.atomic
    def create_user(*, email, password, first_name, last_name, roles=None):
        user = User.objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        if roles:
            user.roles.set(roles)

        return user