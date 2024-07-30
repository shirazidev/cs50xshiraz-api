# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminUserForPost(BasePermission):
    def has_permission(self, request, view):
        # Allow access to non-admins for GET requests
        if request.method == 'GET':
            return True
        
        # Only allow POST requests for admin users
        if request.method == 'POST':
            return request.user and request.user.is_staff
        
        # Deny access for other methods
        return False