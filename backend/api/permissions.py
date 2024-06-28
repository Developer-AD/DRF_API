from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    # def has_object_permission(self, request, view):   
    def has_permission(self, request, view):    
        # if request.method == 'GET':
        if request.user.is_authenticated:
            return True
        return False