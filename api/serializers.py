from rest_framework import serializers as s

from api import models as m
from LinkShortener.settings import HOST


class ShortLinkSerializer(s.ModelSerializer):

    class Meta:
        fields = ("short", "url", "expired")
        model = m.ShortLink

    def to_representation(self, instance):
        self.instance.short = HOST + self.instance.short
        self.instance.expired = "Истекает " + dict(self.instance.EXPIRED_TIME)[self.instance.expired]
        return super(ShortLinkSerializer, self).to_representation(instance)
