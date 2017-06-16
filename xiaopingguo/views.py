# coding:utf-8
from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
import random
import json
from xiaopingguo.serialzers import *
from xiaopingguo.models import User_info
from xiaopingguo.serialzers import *


# Create your views here.




def index(request):
    user_info = User_info.objects.all().order_by('-create_time')
    if len(user_info) == 0:
        up_score = 150
        surplus_apple = '9999'
    else:
        surplus_num = user_info[0].surplus_apple
        if int(surplus_num) >= 9000:
            up_score = 150
        elif 9000 > int(surplus_num) >= 6000:
            up_score = 168
        elif 6000 > int(surplus_num) >= 5000:
            up_score = 180
        elif 5000 > int(surplus_num) >= 2000:
            up_score = 200
        elif 2000 > int(surplus_num) >= 1000:
            up_score = 228
        elif 1000 > int(surplus_num) >= 0:
            up_score = 300
    return render(request, 'index.html', {'surplus_apple': int(surplus_num), 'up_score': up_score})


def register(request):
    return render(request, 'register.html')


def new_year(request):
    return render(request, 'new_year.html')


class UserListView(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        user_info = User_info.objects.all().order_by("-create_time")
        serializer = User_infoSerializer(user_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK, )

    @csrf_exempt
    def post(self, request, formaty=None):

        print("123")
        try:
            data = request.data
        except Exception as e:
            print(e)
        # print(data)
        # print()
        # print("123")
        t = data.keys()[0]
        # print(unicode(t))
        # print(type(t))
        # s = t.encode("utf-8")
        # print(s)
        # print(type(s))
        # print(json.loads(t.encode("utf-8")))
        # print(type(json.loads(s)[0]))
        # print(json.loads(s)[0]['name'])
        data_new = json.loads(t.encode("utf-8"))
        # print(data_new[0]['name'])
        # print(data.keys()[0])

        user_old = User_info.objects.all().order_by('-create_time')
        if len(user_old) == 0:
            apple_num_old = data_new[0]["surplus_apple"]
        else:
            apple_num_old = user_old[0].surplus_apple
        if apple_num_old == 0:
            return HttpResponse('300,奖品已领取完,谢谢参与！,' + str(apple_num_old), )
        else:
            # print(data_new[0]['name'])
            # print(apple_num_old)
            serializer = User_infoSerializer(data=data_new, many=True)
            if serializer.is_valid():
                # print(serializer.data)
                user_info = User_info.objects.filter(phone=data_new[0]["phone"])
                # print(len(user_info))
                if len(user_info) == 0:
                    serializer.save()
                    a_num = random.randint(50, 100)
                    apple_num_s = int(apple_num_old) - a_num
                    if apple_num_s <= 50:
                        apple_num = 0
                    else:
                        apple_num = apple_num_s
                    user_now = User_info.objects.get(phone=data_new[0]["phone"])
                    user_now.surplus_apple = apple_num
                    user_now.save()
                    return HttpResponse('100,操作成功,' + str(apple_num), )
                else:
                    # print("该号码已领取过")
                    return HttpResponse('200,该号码已领取过,' + str(apple_num_old), )
            else:
                return Response({'surplus_apple': apple_num_old, 'msg': serializer.errors, 'status': 101},
                                status=status.HTTP_400_BAD_REQUEST, )
