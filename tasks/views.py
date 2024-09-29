from django.shortcuts import render, redirect
from django.views import View
from tasks.models import Task, Category
from tasks.forms import TaskForm
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView

def main_page_view(request):
    return render(request, 'base.html')
class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')

        if search:
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search))

        if category:
            queryset = queryset.filter(category__id=category)

        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_create.html'