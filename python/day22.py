def calcscore(cards):
    winning,score=cards[1] if len(cards[1])>0 else cards[0], 0
    while len(winning) > 0: score+=len(winning)*winning.pop(0)
    return score

def playgame(cards,recursivecombat):
    state=[[],[]]
    while all([True if len(set)>0 else False for set in cards]):
        if cards[0] in state[0] and cards[1] in state[1]: cards[1].clear()
        else:
            for i in range(2): state[i].append(cards[i].copy())
            card1,card2=cards[0].pop(0),cards[1].pop(0)
            if recursivecombat and card1<=len(cards[0]) and card2<=len(cards[1]):
                sub1,sub2=playgame((cards[0].copy()[:card1],cards[1].copy()[:card2]),True)
                playerwins=1 if len(sub1)>0 else 2
            else: playerwins=1 if card1>card2 else 2
            cards[playerwins-1].append(card1 if playerwins==1 else card2)
            cards[playerwins-1].append(card2 if playerwins==1 else card1)
    return cards
lines,cards,currentplayer=[line.strip() for line in open("../input/day22.txt")],[[],[]],0
for line in lines:
    if 'Player' in line: currentplayer=int(line[-2:-1])
    elif len(line)>0: cards[currentplayer-1].append(int(line))
print(calcscore(playgame((cards[0].copy(),cards[1].copy()),False)))
print(calcscore(playgame((cards[0],cards[1]),True)))
