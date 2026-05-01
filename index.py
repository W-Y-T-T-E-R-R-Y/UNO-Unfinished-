#skip=10
#+2=11
#king=12
#+4=13
import random
import sys

global_card=[['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',0],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',1],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',2],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',3],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',4],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',5],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',6],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',7],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',8],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['blue',9],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',0],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',1],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',2],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',3],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',4],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',5],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',6],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',7],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',8],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['yellow',9],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',0],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',1],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',2],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',3],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',4],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',5],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',6],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',7],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',8],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['red',9],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',0],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',1],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',2],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',3],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',4],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',5],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',6],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',7],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',8],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',9],['green',10],['green',10],['red',10],['red',10],['blue',10],['blue',10],['yellow',10],['yellow',10],['green',11],['green',11],['red',11],['red',11],['blue',11],['blue',11],['yellow',11],['yellow',11],['black',12],['black',12],['black',12],['black',12],['black',13],['black',13],['black',13],['black',13]]
discard=[['black',14]]
player1card=[]
player2card=[]
colormap={'blue':'蓝','yellow':'黄','green':'绿','red':'红','black':'黑'}
cardmap={10:"跳过",11:"+2",12:"王牌",13:"+4"}
playerinmain=1
dangqianmy=1
def fapai(num,player):
    for i in range(num):
        player.append(global_card[random.randint(0, len(global_card) - 1)])
    return player
def player1_play_a_card(dangqian:int):
    print('player' + '1' + 'please!')
    print('you have:')
    for i in player1card:
        print(colormap[i[0]], end='')
        if i[1] > 9:
            print(cardmap[i[1]])
        else:
            print(i[1])
    try:
        index = int(input())-1
    except ValueError:
        fapai(1,player1card)
        global dangqianmy
        dangqianmy -= 1
        return 0
    discard.append(player1card[index])
    player1card.pop(index)
    if discard[dangqian][0]== 'black':
        if discard[dangqian][1] == 13:
            fapai(4, player2card)
        discard.pop(-1)
    elif discard[dangqian-1][0]== 'black':
        return 0
    elif discard[dangqian][0]==discard[dangqian - 1][0] or discard[dangqian][1]==discard[dangqian - 1][1]:
        return 0
    else:
        print('ERROR')
        sys.exit()
def player2_play_a_card(dangqian:int):
    print('player' + '2' + 'please!')
    print('you have:')
    for i in player2card:
        print(colormap[i[0]], end='')
        if i[1] > 9:
            print(cardmap[i[1]])
        else:
            print(i[1])
    try:
        index = int(input())-1
    except ValueError:
        fapai(1,player2card)
        global dangqianmy
        dangqianmy-=1
        return 0
    discard.append(player2card[index])
    player2card.pop(index)
    if discard[dangqian][0]== 'black':
        if discard[dangqian][1]==13:
            fapai(4,player2card)
        discard.pop(-1)
    elif discard[dangqian][0]==discard[dangqian - 1][0] or discard[dangqian][1]==discard[dangqian - 1][1]:
        return 0
    else:
        print('ERROR')
        sys.exit()
fapai(7,player1card)
fapai(7,player2card)
while True:
    playerinmain+=1
    if playerinmain==3:
        playerinmain=1
    player1_play_a_card(dangqianmy)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if len(player1card)==0 or len(player2card)==0:
        break
    print(colormap[discard[-1][0]], end='')
    if discard[-1][1] > 9:
        print(cardmap[discard[-1][1]])
    else:
        print(discard[-1][1])
    dangqianmy+=1
    player2_play_a_card(dangqianmy)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    if len(player1card)==0 or len(player2card)==0:
        break
    print(colormap[discard[-1][0]], end='')
    if discard[-1][1] > 9:
        print(cardmap[discard[-1][1]])
    else:
        print(discard[-1][1])
    dangqianmy+=1
if len(player1card)==0:
    print('player1 won!')
else:
    print('player2 won!')