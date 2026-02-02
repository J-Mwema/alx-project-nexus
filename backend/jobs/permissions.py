from rest_framework.permissions import BasePermission
from users.models import User


class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.EMPLOYER
        )

class IsJobOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.employer == request.user

