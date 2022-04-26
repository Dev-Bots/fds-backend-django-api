from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user

class IsClubOrScoutEditRetrive(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'GET'] and request.user == obj:
            if request.data:
                if request.method == 'PATCH' and 'is_assigned' in request.data['more'].keys():
                    return False
            return True
        return obj.more.club == request.user

class IsClub(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'CLUB'

class IsPlayer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'Player'

class IsScout(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.type == 'Scout'

class FirstTimeApplication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user not in obj.applicants.all()

