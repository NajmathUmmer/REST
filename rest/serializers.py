from rest_framework import serializers
from .models import AvailableBooks

class AvailableBooksSerializer(serializers.ModelSerializer):
 	

 	class Meta:
 		model = AvailableBooks
 		fields = '__all__'