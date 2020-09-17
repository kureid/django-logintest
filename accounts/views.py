from django.shortcuts import render
from .models import Player
from . import forms


def login(request):
    message = ''
    f = forms.LoginForm()
    if request.method == 'POST':
        if 'user_name' in request.POST:
            name = request.POST.get('user_name')
            mail = request.POST.get('user_mail')
            if Player.objects.filter(user_name=name, user_mail=mail).exists():
                p = Player.objects.get(user_name=name, user_mail=mail)
                p.use = True
                p.save()
                print(p.pid)
            else:
                message = '入力されたユーザ情報は存在しませんでした．ユーザ登録をしてください．'

    context = {
        'form': f,
        'message': message
    }
    return render(request, 'accounts/login.html', context)


def sign_up(request):
    message = ''
    f = forms.LoginForm()
    if request.method == 'POST':
        p = Player(color="null", user_name=request.POST.get(
            'user_name'), user_mail=request.POST.get('user_mail'))
        p.save()
        message = 'ユーザ登録が完了しました．ログインしてください．'
        return render(request, 'accounts/login.html')
    context = {
        'form': f,
        'message': message
    }
    return render(request, 'accounts/sign_up.html', context)


def logout(request):
    p = Player.objects.get(pid=pid)
    if p.use:
        message = 'ログアウトが完了しました．'
        p.use = False
        p.save()
    else:
        message = 'ログインされていませんでした．'
    context = {
        'message': message
    }
    return render(request, 'accounts/login.html', context)
