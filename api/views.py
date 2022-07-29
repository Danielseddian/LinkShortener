from django.http import request as Request
from django.shortcuts import get_object_or_404, HttpResponse, redirect, Http404
from rest_framework.viewsets import GenericViewSet, mixins
from datetime import datetime as dt, timedelta as td, timezone as tz

from api import serializers as s, models as m
from LinkShortener.settings import TIME_ZONE


class CreateShortLinkViewSet(GenericViewSet, mixins.CreateModelMixin):
    """Allows to create a short link for a long one."""

    serializer_class = s.ShortLinkSerializer


def redirector(request: Request, short: str) -> HttpResponse:
    """Redirect to origin url if exists else return 404 response"""
    link: m.ShortLink = get_object_or_404(m.ShortLink, short=short)
    if dt.now().astimezone(tz.utc) > link.created + td(hours=link.expired):
        raise Http404("Expired link")

    ip: str = request.META.get("HTTP_X_FORWARDED_FOR", "").split(",")[0] or request.META.get("REMOTE_ADDR")
    device: str = request.META.get("HTTP_USER_AGENT", "Unknown")[:251]
    m.LinkClick(link=link, ip=ip, device=device).save()

    url: str = link.url
    url += ("&" if url.find("?") + 1 else "?") + "&".join(f"{key}={value}" for key, value in request.GET.items())
    return redirect(url)
