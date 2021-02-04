from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self,request,view,obj):
        return ((obj.owner == request.user) | request.user.is_superuser)