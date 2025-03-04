from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    updated_at = serializers.SerializerMethodField(read_only=True)
    full_story = serializers.SerializerMethodField(read_only=True)

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Story
        fields = ('id', 'author', 'title', 'content','full_story' ,'updated_at')

    def get_updated_at(self,story):
        return story.updated_at.strftime('%Y-%m-%d %H:%M:%S')

    def get_full_story(self,story):
        return story.get_absolute_url()