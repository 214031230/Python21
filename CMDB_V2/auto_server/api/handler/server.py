#!/usr/bin/env python3
from stark.service.stark import StarkConfig, get_choice_text
from django.utils.safestring import mark_safe
from api import models


class ServerConfig(StarkConfig):
    def display_detail(self, row=None, header=False):
        """
        查看详细
        :param row:
        :param header:
        :return:
        """
        if header:
            return "查看详细"
        return mark_safe("<a href='/stark/api/server/%s/detail/'>查看详细</a>" % row.id)

    list_display = [
        StarkConfig.display_checkbox,
        "hostname",
        display_detail,
        get_choice_text('device_status_id', '状态'),
    ]

    search_list = ["hostname", "business_unit__name"]

    def multi_delete(self, request):
        pks = request.POST.getlist("pk")
        models.Server.objects.filter(id__in=pks).delete()

    multi_delete.text = "批量删除"

    action_list = [
        multi_delete,
    ]