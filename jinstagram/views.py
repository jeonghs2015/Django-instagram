from django.shortcuts import render
from rest_framework.views import APIView

class Sub(APIView):
    def get(self, request):
        print("get으로 호출")
        return render(request, "jinstagram/main.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "jinstagram/main.html")