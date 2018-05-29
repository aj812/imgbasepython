from django.contrib.auth.models import User
from rest_framework import serializers
from media.models import Media


class MediaUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "date_joined")


class MediaSerializer(serializers.ModelSerializer):
    user = MediaUserSerializer(read_only=True)

    class Meta:
        model = Media
        fields = ("user", "mediatype", "path", "tags", "date_created")
