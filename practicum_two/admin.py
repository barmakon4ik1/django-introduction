from django.contrib import admin
from .models import *


def replace_spaces_with_underscores(self, request, objects):
    for obj in objects:
        obj.title = obj.title.replace(' ', '_')
        obj.save()
    return objects


def change_priority_to_low(self, request, objects):
    for obj in objects:
        obj.priority = 'Low'
        obj.save()
    return objects


def change_priority_to_medium(self, request, objects):
    for obj in objects:
        obj.priority = 'Medium'
        obj.save()
    return objects


def change_priority_to_high(self, request, objects):
    for obj in objects:
        obj.priority = 'High'
        obj.save()
    return objects


def change_priority_to_very_high(self, request, objects):
    for obj in objects:
        obj.priority = 'Very High'
        obj.save()
    return objects


change_priority_to_low.short_description = 'Mark as Low priority'
change_priority_to_medium.short_description = 'Mark as Medium priority'
change_priority_to_high.short_description = 'Mark as High priority'
change_priority_to_very_high.short_description = 'Mark as Very High priority'
replace_spaces_with_underscores.short_description = 'Replace spaces with underscores'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at', 'due_date')
    search_fields = ('title',)
    list_filter = ('status', 'priority', 'project', 'created_at', 'due_date')
    actions = [
        change_priority_to_low,
        change_priority_to_medium,
        change_priority_to_high,
        change_priority_to_very_high,
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    search_fields = ('title',)
    actions = [replace_spaces_with_underscores]


@admin.register(ProjectFile)
class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'created_at')
    search_fields = ('title', )
    list_filter = ('created_at',)
