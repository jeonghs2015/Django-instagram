from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        return render(request, "jinstagram/main.html")
