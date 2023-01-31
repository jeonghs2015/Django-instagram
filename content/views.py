from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by("-id")  # select * from content_feed

        return render(request, "jinstagram/main.html", context=dict(feed_list=feed_list))

class UploadFeed(APIView):
    def post(self, request):
        file = request.data.get('file')
        image = request.data.get('image')

        print(file)
        print(image)

        return Response(status=200)
