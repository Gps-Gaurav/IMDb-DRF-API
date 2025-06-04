from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    message = 'admin or read only'
    
    # uesd for listing only (usually action are not taken)
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        admin_permission = super().has_permission(request=request, view=view)
        if request.method == 'GET' or admin_permission:
            return True
        return False
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.review_user == request.user:
                return True
            else:
                return False
        # Write permissions are only allowed to the owner of the snippet.
     