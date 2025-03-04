from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer
from .permissions import IsOwnerOrReadOnly


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
