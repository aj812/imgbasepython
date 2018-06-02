from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse
from django.shortcuts import render
import simplejson as json

from media.models import Media
from media.permissions import UserIsOwnerMedia
from media.serializers import MediaSerializer



def SearchImgsView(request):
    testarr = ['blah', 'fifth']
    images = Media.objects.all()
    overlapfilter = Media.objects.all().filter(tags__overlap=testarr)
    first = images[0]
    context = {
        "images": images,
        "overlapfilter": overlapfilter,
        "terms": testarr,
    }
    jsonres = json.dumps({ 'id': first.id, 'filename': first.filename, 'mediatype': first.mediatype, 'tags': first.tags, 'uri': first.uri })
    # return HttpResponse(first.uri)
    return render(request, 'media/media_list.html', { 'terms': testarr, 'overlapfilter': overlapfilter, 'images': images, 'jsonres': jsonres })

# def SearchImgsView(request):
#     html = "<html><body> Hello </body></html>"
#     return HttpResponse(html)


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
