from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Book
from .serializers import ThingSerializer
from .permissions import OwnerOnly

class bookListCreateView(ListCreateAPIView):
    
    queryset=Book.objects.all()
    serializer_class=ThingSerializer


class bookDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=ThingSerializer
    permission_classes=[OwnerOnly]