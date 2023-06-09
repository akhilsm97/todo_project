from django.urls import path, include
from .import views
app_name = 'app_1'

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update, name="update"),
]