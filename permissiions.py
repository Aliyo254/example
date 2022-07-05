from rest_framework.permissions import BasePermission


class IsElder(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_elder)


class IsResident(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_resident)


class IsController(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_controller)