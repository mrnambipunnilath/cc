from django.shortcuts import render

# Create your views here.
# myapi/views.py 
from rest_framework import viewsets 
from .serializers import CharacterSerializer 
from .models import Character 
class CharacterViewSet(viewsets.ModelViewSet): 
	queryset = Character.objects.all().order_by('name') 
	serializer_class = CharacterSerializer # This is from step 4.3
