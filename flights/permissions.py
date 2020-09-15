from rest_framework.permissions import BasePermission
import datetime


class IsOwner(BasePermission):
    message = "You must be the owner of this booking."

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class IsAble(BasePermission):
    message = "TOO LATE!! you cannot cancel or update your booking now"

    def has_object_permission(self, request, view, obj):
        if (obj.date - datetime.date.today()).days >= 3:
            return True
        else:
            return False
