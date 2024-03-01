from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import FormView,ListView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .forms import TaskForm,EditForm
from .models import TaksModel

# Create your views here.
def home(req):
    return render(req, 'home.html')
class TaskView(ListView):
    template_name = 'home.html'
    model = TaksModel
    context_object_name = 'todos'
    def get_queryset(self):
        return TaksModel.objects.filter(is_completed = False)
def completed(req):
    return render(req, 'completed.html')
class CompleteTaskView(ListView):
    template_name = 'completed.html'
    model = TaksModel
    context_object_name = 'todos'
    def get_queryset(self):
        return TaksModel.objects.filter(is_completed = True)

class TaksStoreFormView(FormView):
    template_name = 'add_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('home')
    def form_valid(self,form):
        print(form.cleaned_data)
        form.save()
        return redirect('home')

class DeleteTask(DeleteView):
    model = TaksModel
    template_name = 'confirmation.html'
    success_url = reverse_lazy('home')
class EditTask(UpdateView):
    model = TaksModel
    template_name = 'edit_task.html'
    form_class = EditForm
    success_url = reverse_lazy('home')
def complete_task(req,id):
    data = TaksModel.objects.get(id = id)
    data.is_completed = True
    data.save()
    return redirect('completed')

