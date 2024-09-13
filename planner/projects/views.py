from django.shortcuts import render

# Create your views here.
# projects/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class SecureDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {"message": "This is a protected resource"}
        return Response(data)
