from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Player,Room
# Create your views here.

def addid(request):
    if request.session.get('nickname',) != None:
        return HttpResponse("<script>alert('이미 접속된 아이디입니다.'); history.go(-1);</script>");
    return render(request, 'network/ID.html', {})

def register(request):
    print(request.session.get('nickname',))
    if request.session.get('nickname',) == None:
        try:
            nickname=request.POST['nickname']
            nickname=nickname.strip()
            if nickname == "":
                raise NameError #ID를 설정 안했을 경우
            new_player=Player(nickname=nickname)
            new_player.save()
            request.session['nickname'] = nickname
        except NameError:
            return HttpResponse("<script>alert('닉네임을 입력하지 않았습니다. 다시 입력해주세요.'); history.go(-1);</script>");
        except:
            return HttpResponse("<script>alert('아이디 중복입니다.'); history.go(-1);</script>");
            print(request.session.get('nickname',))
        return render(request, 'network/introdution.html', {})
    print(request.session.get('nickname',))
    return render(request, 'network/introdution.html', {})
def roomlist(request):
    print(request.session.get('nickname',))
    rooms = Room.objects.all()
    return render(request, 'network/room_list.html', {'rooms':rooms})

def room(request):
    if request.session.get('nickname',) == None:
        return render(request, 'network/ID.html', {}) #아아디가 없을 경우

    nn = request.session.get('nickname',) #접속한 아이디
    player=Player.objects.get(nickname=nn)

    if(player.is_joined==True):#방에 입장 중인 아이디
        return HttpResponse("<script>alert('방 입장된 아이디 입니다.'); history.go(-1);</script>");
    if(Room.objects.filter(current_player_number = 1).count()==0):#방이 없을 경우
        new_room = Room.objects.create(name=nn, current_player_number=1)
        player=Player.objects.get(nickname=nn)
        player.is_joined=True
        new_room.join_players.add(player)
        new_room.save()
        player.save()
        #return HttpResponse("방 생성 완료")
        return HttpResponseRedirect('/room/%s/' % new_room.name)
    else: #방이 있을 경우
        room = Room.objects.get(current_player_number = 1)
        room.current_player_number += 1
        player=Player.objects.get(nickname=nn)
        player.is_joined=True
        room.join_players.add(player)
        room.save()
        player.save()
        #return HttpResponse("방 입장 완료")
        return HttpResponseRedirect('/room/%s/' % room.name)
    return render(request, 'network/room.html', {})

def game(request,name):
    room=Room.objects.get(name=name)
    if(room.current_player_number==1):
            return render(request, 'network/waiting.html', {'name':name})
    return render(request, 'network/game.html', {'name':name})
