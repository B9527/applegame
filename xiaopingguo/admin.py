# coding:utf-8
from django.contrib import admin
from xiaopingguo.models import *


# Register your models here.

class User_infoAdmin(admin.ModelAdmin):
    # ...
    search_fields = ['score', 'name']
    ordering = ('-create_time',)  # 排序
    list_filter = ('score', 'create_time', 'surplus_apple')
    fieldsets = (
        (None, {
            'fields': ('type', 'name', 'score', 'surplus_apple', 'add_more')
        }),
        ('用户个人信息', {
            'classes': ('collapse',),
            'fields': ('phone', 'address',)
        }),
    )


admin.site.register(User_info, User_infoAdmin)
