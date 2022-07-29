from bulk_update_or_create import BulkUpdateOrCreateQuerySet
from django.core import validators as v
from django.db import models as m

from api.utilits import generate_string, List


class ShortLink(m.Model):
    """Short link model"""

    EXPIRED_TIME = (
        (1, "через 1 час"),
        (4, "через 4 часа"),
        (12, "через 12 часов"),
        (24, "через 1 сутки"),
        (96, "через 4 суток"),
        (168, "через 1 неделя"),
        (720, "через 1 месяц (30 дней)"),
        (8_760, "через 1 год (365 дней)"),
    )

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    short = m.CharField(
        max_length=10,
        validators=(v.MinLengthValidator(3), v.MaxLengthValidator(10)),
        db_index=True,
        unique=True,
        default=generate_string(),
        blank=True,
        null=True,
        verbose_name="сокращение",
    )
    url = m.URLField(max_length=128, verbose_name="оригинальная ссылка")
    created = m.DateTimeField(auto_now=True, verbose_name="когда создана")
    expired = m.PositiveSmallIntegerField(choices=EXPIRED_TIME, verbose_name="когда истекает")

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            exists = ShortLink.objects.values_list("short", flat=True)
            self.short: str = generate_string(excludes=exists) if self.short in exists else self.short
        super().save(force_insert, force_update, using, update_fields)


class LinkClick(m.Model):
    """Link visitor's statistic model"""

    objects = BulkUpdateOrCreateQuerySet.as_manager()

    link = m.ForeignKey(ShortLink, on_delete=m.CASCADE, related_name="statistic", verbose_name="ссылка")
    ip = m.GenericIPAddressField(verbose_name="IP-адрес посетителя")
    device = m.CharField(max_length=250, verbose_name="устройство")
    linked_time = m.DateTimeField(auto_now=True, verbose_name="время перехода по ссылке")

    class Meta:
        verbose_name = "Информация о переходе по ссылке"
        verbose_name_plural = "Статистика переходов по ссылкам"
