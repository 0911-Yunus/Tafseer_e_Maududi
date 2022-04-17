from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ChapterSerializer
from .models import Chapter

# Create your views here.


class ChapterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
