from uuid import uuid4
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feed
import os
from jinstagram.settings import MEDIA_ROOT

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by("-id")  # select * from content_feed

        return render(request, "jinstagram/main.html", context=dict(feed_list=feed_list))

class UploadFeed(APIView):
    def post(self, request):

        file = request.FILES['file']

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        file = request.data.get('file')
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        return Response(status=200)
