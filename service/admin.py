from django.contrib import admin

from service.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "datetime_field", "deadline", "task_done"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", ]
