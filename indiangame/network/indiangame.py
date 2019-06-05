import random

turn = 0;
stack = 0;
gcont = True;
def Firststart(A, B):
	A, B = Initialize(A, B);# 초기화

def Gamestart(A, B, turn, stack, gcont):
	if gcont == True: # 게임 한 세트가 종료 됐을 시 실행
		A,B=Matchstart(A,B); # 매치 시작, 기본으로 칩 1개 베팅
		A.card = Randomcard();
		B.card = Randomcard();
	if Endcheck(A, B) == 1: # 칩이 0인 유저 확인
		return A, B, turn, stack, gcont;
	Printscore(A,B,stack); # 현재 점수 출력
	Player, Ene = Turn(A, B, turn); # 턴 계산
	Cardopen(Ene); # 상대방의 카드 공개
	Printbet(A,B); # 칩 베팅 현황 출력
	cmd, turn, gcont = Betinput(Player, Ene, turn, gcont);
	# 베팅한 결과에 따라, cmd, turn 리턴
	if cmd == 'err': # 입력에 오류 있을 시 실행
		Err();
	elif cmd == 'lose': # 0개 배팅, 게임 종료
		Player, Ene, stack, gcont = Lose(Player, Ene, stack, gcont);
	elif cmd == 'over': # 상대와 동일하게 배팅
		Player, Ene, stack, gcont = Over(Player, Ene, stack, gcont);
	if cmd != 'err': #
		print("★★★★★★★★★★★★★★★★★★★★");
		Printscore(A,B,stack); # 현재 점수 출력
		print("★★★★★★★★★★★★★★★★★★★★");
	return A, B, turn, stack, gcont;

class Playerdata:
   card = int(0); # 현재 카드
   chip = int(0); # 현재 보유 칩
   bet = int(0); # 플레이어가 베팅에 건 칩

def Randomcard(): # 1~10 의 숫자중 난수 하나 리턴
      Cardarr = [1,2,3,4,5,6,7,8,9,10];
      return random.sample(Cardarr,1)[0];

def Initialize(A): # 게임 처음 시작 시 초기화
	A.chip = int(29);
	A.bet =  int(1);
	A.card = Randomcard();
	A.is_show_result = 0;

def Matchstart(A, B): # 매치 시작시 칩 1개 배팅
	A.chip -= 1;
	B.chip -= 1;
	A.bet += 1;
	B.bet += 1;
	A.prev_card = A.card;
	B.prev_card = B.card;
	A.card = Randomcard();
	B.card = Randomcard();

def Endcheck(A, B): # 칩 0 인 유저 있을 시 게임 종료
	if A.chip + A.bet <= 0:
		#print("B플레이어 우승");
		return A;
	elif B.chip + B.bet <= 0:
		#print("A플레이어 우승");
		return B;
	else:
		return False;

def SetTurn(A, B):
        if A.is_my_turn == True:
                A.is_my_turn = False
                B.is_my_turn = True
        else:#A.is_my_turn == False일 경우. 즉, B.is_my_turn == True일경우
                A.is_my_turn = True
                B.is_my_turn = False



def Betinput(player, match_player, bet):
		if int(bet) == 0:
			return 1
		elif player.bet + int(bet) < match_player.bet:
			return 1
		elif player.bet + int(bet) > match_player.bet:
			if player.chip < int(bet) :
                                return 2
				#print("사용 가능한 칩의 갯수를 초과했습니다");
			elif int(bet) >= match_player.chip + match_player.bet:
                                return 3
				#print("상대방의 칩의 갯수보다 적게 입력 해야 합니다.");
			else:
				player.bet = player.bet + int(bet);
				player.chip = player.chip - int(bet);
				return 0
		elif player.bet + int(bet) == match_player.bet:
			player.bet += int(bet);
			player.chip -= int(bet);
			return 0


def Lose(player, match_player, stack):
	match_player.chip += player.bet + match_player.bet + stack;
	player.bet = match_player.bet = 0;
	if player.card == 10:
		#print("플레이어의 카드가 10이었으므로 패널티");
		player.chip -= 10;
		match_player.chip += 10;
	player.is_show_result = 2;
	match_player.is_show_result = 1;

def Over(player, match_player, stack):
	if player.card == match_player.card: # 무승부
		stack = player.bet + match_player.bet;
		player.is_show_result = 3;
		match_player.is_show_result = 3;
		#print("무승부입니다.");
	elif player.card > match_player.card:
		player.chip += player.bet + match_player.bet + stack;
		stack = 0;
		player.is_show_result = 1;
		match_player.is_show_result = 2;
		#print(Player.name,"님이 우승하셨습니다.");
	elif player.card < match_player.card:
		match_player.chip += player.bet + match_player.bet + stack;
		stack = 0;
		player.is_show_result = 2;
		match_player.is_show_result = 1;
		#print(Ene.name,"님이 우승하셨습니다.");
	player.bet = match_player.bet = 0;
	return int(stack)
