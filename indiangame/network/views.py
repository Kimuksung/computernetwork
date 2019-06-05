from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Player,Room
from .indiangame import *
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
    match_player=False
    waiting=False
    room=Room.objects.get(name=name)
    session_nickname = request.session.get('nickname',)
    player = Player.objects.get(nickname = session_nickname)
    for room_player in room.join_players.all(): #Player match_player 나누기
        if room_player.nickname != session_nickname: #Player
            match_player = room_player

    if(room.is_playing==True):
        lose_player = Endcheck(player, match_player)
        if lose_player:#패배한 플레이어가 있다면,
            HttpResponse("패배한 플레이어 존재")
    elif(player.is_my_turn==True):
        try:
            print('test3')
            is_bet = Betinput(player, match_player, request.POST['bet'])
            if is_bet == 0:
                #배팅액이 같을 경우 승패를 판단해 적용시킨다.
                if player.bet == match_player.bet:
                    room.stack = Over(player, match_player, room.stack)
                    Matchstart(player, match_player)

                    #턴을 설정한다.
                    SetTurn(player, match_player)
                    match_player.save()
                elif is_bet == 1:
                    return HttpResponse(
                    "<script>alert('상대방이 배팅한 칩보다 많은 칩을 입력해야 합니다.'); history.go(-1);</script>");
                elif is_bet == 2:
                    return HttpResponse(
                    "<script>alert('사용 가능한 칩의 갯수를 초과했습니다.'); history.go(-1);</script>");
                elif is_bet == 3:
                    return HttpResponse(
                    "<script>alert('상대방의 칩의 갯수보다 적게 입력해야 합니다.'); history.go(-1);</script>");

        except:
            if 'die' in request.POST:
                print('test3')
                SetTurn(player, match_player)
                Lose(player, match_player, room.stack)
                Matchstart(player, match_player)
                room.stack = 0
                match_player.save()
    else:
        waiting=True

    if(room.current_player_number==1):#대기방
            return render(request, 'network/waiting.html', {'name':name})

    if(room.current_player_number==2 and room.is_playing==False):#게임 시작 하기 전 기본 값 세팅
        print('initialize first')
        room.is_playing=True
        Initialize(player)
        Initialize(match_player)
        player.save()
        match_player.save()
        temp = Player.objects.get(nickname=room.name)
        temp.is_my_turn=True
        temp.save()
        return render(request, 'network/game.html', {'player':player,'room':room,'match_player':match_player})
