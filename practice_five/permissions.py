from rest_framework.permissions import BasePermission


class IsCustomerOrReadOnly(BasePermission):
    """
    Разрешает редактирование объектов только их владельцам (customer), остальным - только чтение.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.customer.email == request.user.email


class CanViewStatistics(BasePermission):
    """
    Разрешает доступ к статистике только пользователям с соответствующим разрешением.
    """
    def has_permission(self, request, view):
        return request.user.has_perm('practice_five.can_view_statistics')

