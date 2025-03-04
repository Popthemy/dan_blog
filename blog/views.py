from rest_framework import viewsets
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from .models import Story
from .models import Story
from .serializers import StorySerializer
# Assuming this permission class is already defined
from .permissions import IsOwnerOrReadOnly


class StoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the CRUD operations for `Story` model.
    The viewset allows authenticated users to create, retrieve, update, and delete their own stories.
    Unauthorized users can only view stories.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @swagger_auto_schema(operation_description="Retrieve a list of stories")
    def list(self, request, *args, **kwargs):
        """
        Retrieve the list of stories.

        If the user is authenticated, they can see all stories, otherwise, only publicly available ones.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific story")
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve the details of a specific story by its ID.
        """
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new story")
    def create(self, request, *args, **kwargs):
        """
        Create a new story. Only authenticated users can create stories.
        """
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update an existing story")
    def update(self, request, *args, **kwargs):
        """
        PUT:
        Update a story. Only the owner of the story can update it.
        """
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Partially update an existing story")
    def partial_update(self, request, *args, **kwargs):
        """
        PATCH:
        Update a story partially. Only the owner of the story can partially update it.
        """
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a story")
    def destroy(self, request, *args, **kwargs):
        """
        Delete a story. Only the owner of the story can delete it.
        """
        return super().destroy(request, *args, **kwargs)
