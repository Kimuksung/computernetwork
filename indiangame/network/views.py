from django.shortcuts import render
from django.http import HttpResponse
from .models import Player,Room
# Create your views here.
def addid(request):
    return render(request, 'network/ID.html', {})

def register(request):
    try:
        nickname=request.POST['nickname']
        nickname=nickname.strip()
        if nickname == "":
            raise NameError #ID를 설정 안했을 경우
        new_player=Player(nickname=nickname)
        new_player.save()
        #return HttpResponse("완료")
    except NameError:
        return HttpResponse("<script>alert('닉네임을 입력하지 않았습니다. 다시 입력해주세요.'); history.go(-1);</script>");
    except:
        return HttpResponse("<script>alert('아이디 중복입니다.'); history.go(-1);</script>");
    return render(request, 'network/introdution.html', {})

def roomlist(request):
    rooms = Room.objects.all()
    #print(rooms)
    return render(request, 'network/room_list.html', {'rooms':rooms})
