from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from member.forms import LoginForm


def login_fbv(request):
    if request.method == 'POST':
        # html파일에서 POST요청을 보내기위해서
        # from을 정의하고 input요소 2개의 name을
        # username, password로 설정하고
        # button type submit사용
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # 전달되어온 POST데이터에서 'username'과 'password'키의 값들을 사용
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # authenticate의 인자로 POST로 전달받은 username, password를 사용
            user = authenticate(username=username, password=password)

            # 만약 인증이 정상적으로 완료되었다면
            # (해당하는 username, password에 이맃하는 User객체가 존재할경우
            if user is not None:
                # Django의 인증관리 시스템을 이용하여 세션을 관리해주기위해 loing() 함수 사용
                login(request, user)
                return redirect('/admin')
            # 인증에 실패하였다면 (username, password에 일치하는 User객체가 존재하지 않을 경우
            else:
                form.add_error(None, 'ID or Pw incorrects')
                # GET method로 요청이 왔을 경우
    else:
        form = LoginForm()

    context = {
        'form': form,
    }  # member/login
    return render(request, 'member/login.html', context)
