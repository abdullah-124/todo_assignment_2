from django.db import models

# Create your models here.
class TaksModel(models.Model):
    id = models.IntegerField(primary_key = True)
    task_title = models.CharField(max_length = 30)
    taskDescription = models.CharField(max_length = 100)
    is_completed = models.BooleanField(default = False)

    def __str__(self) -> str:
        return f"{self.task_title}"
