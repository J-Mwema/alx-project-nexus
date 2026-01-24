from rest_framework.permissions import BasePermission
from users.models import User


class IsEmployerAndJobOwner(BasePermission):
    """
    Only the employer who owns the job
    can update the application status
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.role == User.Role.EMPLOYER
            and obj.job.employer == request.user
        )
