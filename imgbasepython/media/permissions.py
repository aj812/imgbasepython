from rest_framework.permissions import BasePermission


class UserIsOwnerMedia(BasePermission):

    def has_object_permission(self, request, view, media):
        return request.user.id == media.user.id
