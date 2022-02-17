from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ToDoSerializer
from .models import Todo

# Create your views here.
# The viewsets base class provides the implementation for CRUD operations by default.
class TodoView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = Todo.objects.all()