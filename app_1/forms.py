from .models import Task
from django import forms

class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields=[
                "task_name",
                "priority",
                "task_date"
                ]