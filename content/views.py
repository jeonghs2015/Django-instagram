from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()  # select * from content_feed
        print(feed_list)
        return render(request, "jinstagram/main.html")
