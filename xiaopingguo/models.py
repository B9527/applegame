# coding: utf-8

from django.db import models


class User_info(models.Model):
    type = models.CharField(max_length=15, default=u'抽奖', verbose_name='用户类型')
    name = models.CharField(max_length=31, verbose_name='用户姓名')
    phone = models.CharField(max_length=11, verbose_name='用户手机号码')
    address = models.CharField(max_length=250, verbose_name='用户地址')
    create_time = models.DateTimeField(verbose_name=u"用户创建时间", auto_now_add=True)
    add_more = models.CharField(max_length=500, verbose_name=u'备注', blank=True, null=True)
    surplus_apple = models.CharField(max_length=10, verbose_name=u"剩余苹果数", blank=True, null=True)
    score = models.CharField(max_length=10, verbose_name=u'分数', blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = u"用户信息"
        ordering = ['create_time']
