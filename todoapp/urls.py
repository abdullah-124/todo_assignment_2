from django.urls import path 
from . import views

# URL Patterns
urlpatterns = [
    path('',views.TaskView.as_view(), name = 'home'),
    path('completed/',views.CompleteTaskView.as_view(), name = 'completed'),
    path('add_task/', views.TaksStoreFormView.as_view(), name = 'add_task'),
    path('delete/<int:pk>/',views.DeleteTask.as_view(), name = 'delete'),
    path('edit/<int:pk>/',views.EditTask.as_view(), name = 'edit'),
    path('completed/<int:id>/',views.complete_task, name = 'completed'),
]
