from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    if request.method and request.method not in permissions.SAFE_METHODS:

      print(f'>>>>>>>>>> author: {obj.author}  , user:{request.user}    \n >>>>>')
      return bool( obj.author == request.user )
    return super().has_object_permission(request, view, obj)
