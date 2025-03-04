from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Story
        fields = ('id', 'author', 'title', 'content', 'updated_at')

    def get_updated_at(self,story):
        return story.updated_at.strftime('%Y-%m-%d %H:%M:%S')
g