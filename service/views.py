from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag


class Index(generic.ListView):
    model = Task
    template_name = "service/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "service/task_form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("service:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "service/task_form.html"
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("service:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "service/task_confirm_delete.html"
    success_url = reverse_lazy("service:index")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "service/tag_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    template_name = "service/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("service:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    template_name = "service/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("service:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "service/tag_confirm_delete.html"
    success_url = reverse_lazy("service:tags-list")


class TaskChangeStatus(generic.RedirectView):
    model = Task
    template_name = "service/index.html"

    def get_redirect_url(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.task_done = not task.task_done
        task.save()
        return super().get_redirect_url(*args, **kwargs)
