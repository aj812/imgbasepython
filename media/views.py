from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse
from django.shortcuts import render
import simplejson as json

from django.http import JsonResponse
from django.core import serializers

from media.models import Media
from media.permissions import UserIsOwnerMedia
from media.serializers import MediaSerializer



def SearchImgsView(request):
    # Array Querystring: http://localhost:8000/api/media/search/?tags[]=TAGONEHERE&tags[]=TAGTWOHERE
    query = request.GET.getlist('tags[]')
    queryarr = query
    # testarr = ['blah', 'fifth']
    # images = Media.objects.all()
    overlapfilter = Media.objects.all().filter(tags__overlap=queryarr)
    context = {
        "overlapfilter": overlapfilter,
        "terms": queryarr,
    }
    imgs_serialized = serializers.serialize('json', overlapfilter)
    # return render(request, 'media/media_list.html', { 'terms': queryarr, 'overlapfilter': overlapfilter, 'images': images })
    # return JsonResponse({ 'id': first.id, 'filename': first.filename, 'mediatype': first.mediatype, 'tags': first.tags, 'uri': first.uri })
    return HttpResponse(imgs_serialized, content_type='application/json')

class MediaCreateAPIView(ListCreateAPIView):
    serializer_class = MediaSerializer

    def get_queryset(self):
        return Media.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MediaDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
    ## * require Auth
    # permission_classes = (IsAuthenticated, UserIsOwnerMedia)
