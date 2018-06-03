from django.shortcuts import render
from .models import AvailableBooks
from .serializers import AvailableBooksSerializer
from rest_framework import generics


class AvailableBooksList(generics.ListCreateAPIView):
    queryset = AvailableBooks.objects.all()
    serializer_class = AvailableBooksSerializer


class AvailableBooksDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AvailableBooks.objects.all()
    serializer_class = AvailableBooksSerializer
# Create your views here.
