from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from media.models import Media
from media.permissions import UserIsOwnerMedia
from media.serializers import MediaSerializer


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
