from django.contrib import admin
from .models import Story

# Register your models here.


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')
    search_fields = ('title',)
    filter_fields = ('updated_at',)

    class Meta:
        model = Story
