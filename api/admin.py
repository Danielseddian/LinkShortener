from django.contrib import admin as a

from typing import Tuple

from api import models as m


@a.register(m.ShortLink)
class ShortLinkAdmin(a.ModelAdmin):
    editable_fields: Tuple = ("expired",)
    shown_fields: Tuple = ("id", "short", "url", "created")
    all_fields: Tuple = shown_fields + editable_fields

    list_display = all_fields
    list_editable = editable_fields
    list_display_links = shown_fields
    search_fields = all_fields
    list_filter = all_fields


@a.register(m.LinkClick)
class LinkClickAdmin(a.ModelAdmin):
    shown_fields: Tuple = ("id", "link", "ip", "device", "linked_time")

    list_display = shown_fields
    list_display_links = shown_fields
    search_fields = shown_fields
    list_filter = shown_fields

