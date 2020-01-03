# -*- encoding: utf-8 -*-
import copy
import os
from django.http import HttpResponse, Http404
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from post_video_downloading.models import Image
from post_video_downloading.formset import MultiImageForm
from django.db.models.aggregates import Count

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #登入和登出

from django.contrib.auth.decorators import login_required  # 验证用户是否登录

def acc_login(request):


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)  # 类型为<class 'django.contrib.auth.models.User'>

        # print(type(models.Customer.objects.get(name="赵凡")))
        # print(user,type(user))
        if user:

            login(request,user)  # 验证成功之后登录
            return redirect('/index/')
        else:
            return render(request, 'login.html', {'error': "用户名或密码错误！"})

    return render(request, "login.html")


def acc_logout(request):

    logout(request)  # 登出

    return redirect("/login")

@login_required
def check(request):
    return render_to_response("check.html")

@login_required
def reptile(request):
    return render_to_response("reptile-01.html")


@login_required
def reptile_02(request):
    return render_to_response("reptile-02.html")


@login_required
def reptile_03(request):
    return render_to_response("reptile-03.html")


@login_required
def distinguish_01(request):
    return render_to_response("distinguish-01.html")

@login_required
def distinguish_02(request):
    return render_to_response("distinguish-02.html")

@login_required
def distinguish_03(request):
    return render_to_response("distinguish-03.html")

@login_required
def distinguish_04(request):
    return render_to_response("distinguish-04.html")


@login_required
def analysis_01(request):
    return render_to_response("analysis-01.html")


@login_required
def analysis_02(request):
    return render_to_response("analysis-02.html")


@login_required
def index(request):
    return render_to_response('index.html', {"user": request.user.username})

@login_required
def index2(request):
    return render_to_response('index2.html', {"user": request.user.username})

@login_required
def pawan_video_display(request):
    '''
        爬完的视频展示
    :param request:
    :return:
    '''
    sys_dir = r'C:\coding\python\Django_project\video_downloading\post_video_downloading\media\videos\pawan'
    lis = os.listdir(sys_dir)
    items = []
    id_count = 1
    for file in lis:
        file_path = '/media/videos/pawan/'+ file
        file_path_in_system = os.path.join(sys_dir, file)
        if os.path.getsize(file_path_in_system) > 2 * 1024 * 1024:
            '''
            仓鼠不爱玉米粒====我的起源____萌新公会招人====8468418====1573543118.flv
            ['仓鼠不爱玉米粒', '我的起源____萌新公会招人', '8468418', '1573543118.flv']
            '''
            split_list = file.split("====")
            dic = {
                'url': 'http://live.bilibili.com/'+split_list[2],
                'author': split_list[0].replace("____", ' '),
                'path': file_path,
                'name': split_list[1].replace("____", ' '),
                'id': str(id_count)
            }
            items.append(dic)
            id_count += 1

    context = {
        "items": items
    }
    return render_to_response('video_detail_pawan.html', context=context)



@login_required
def detect_finished_and_celebrity_incide(request):

    dic = {
                'url': 'http://www.douyu.com',
                'author': '西门庆',
                'path': '',
                'name': '特朗普总统下野',
                'id': '01'
             }
    context = {
        "items": [
            dic for _ in range(10)
        ]
    }
    return render_to_response('video_detail.html' , context=context)


def test(request):
    return render_to_response('test.html')

@login_required
def upload_picture(request):

    if request.method == 'POST':
        new_img = Image(
            name=request.POST['pic_name'],
            file=request.FILES.get('img')
        )
        print(request.POST['pic_name'])
        new_img.save()
    images = Image.objects.all()

    res = Image.objects.values("name").annotate(num=Count('name'))
    contexts = []
    for dic in res:
        temp_dic = dic
        temp_dic['lis'] = Image.objects.filter(name=dic['name'])[:5]
        contexts.append(copy.deepcopy(temp_dic))

    print([image.name for image in images])
    context = {
        'items': contexts
    }
    return render_to_response("upload_picture.html", context)


def lialan(request):
    sys_dir = r'C:\coding\python\Django_project\video_downloading\post_video_downloading\media\videos\pawan'
    lis = os.listdir(sys_dir)
    items = []
    id_count = 1
    for file in lis:
        file_path = '/media/videos/pawan/' + file
        file_path_in_system = os.path.join(sys_dir, file)
        if os.path.getsize(file_path_in_system) > 2 * 1024 * 1024:
            '''
            仓鼠不爱玉米粒====我的起源____萌新公会招人====8468418====1573543118.flv
            ['仓鼠不爱玉米粒', '我的起源____萌新公会招人', '8468418', '1573543118.flv']
            '''
            split_list = file.split("====")
            dic = {
                'url': 'http://live.bilibili.com/' + split_list[2],
                'author': split_list[0].replace("____", ' '),
                'path': file_path,
                'name': split_list[1].replace("____", ' '),
                'id': str(id_count),
                'roomid': split_list[2]
            }
            items.append(dic)
            id_count += 1

    context = {
        "items": items
    }
    return render_to_response('lialan.html', context=context)

