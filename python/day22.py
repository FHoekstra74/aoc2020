def calcscore(cards):
    winning,score=cards[1] if len(cards[1])>0 else cards[0], 0
    while len(winning) > 0: score+=len(winning)*winning.pop(0)
    return score

def makeidentifier(cards):
    return '.'.join(str(card) for card in cards)

def playgame(cards1,cards2,recursivecombat):
    already1,already2=[],[]
    while len(cards1) > 0 and len(cards2) > 0:
        if makeidentifier(cards1) in already1 and makeidentifier(cards2) in already2: cards2=[]
        else:
            already1.append(makeidentifier(cards1))
            already2.append(makeidentifier(cards2))
            card1,card2=cards1.pop(0),cards2.pop(0)
            if recursivecombat:
                if card1<=len(cards1) and card2<=len(cards2):
                    sub1,sub2=playgame(cards1.copy()[:card1],cards2.copy()[:card2],True)
                    playerwins=1 if len(sub1)>0 else 2
                else: playerwins=1 if card1>card2 else 2
            else: playerwins=1 if card1>card2 else 2
            if playerwins==1:
                cards1.append(card1)
                cards1.append(card2)
            else:
                cards2.append(card2)
                cards2.append(card1)
    return((cards1,cards2))

lines,cards,currentplayer=[line.strip() for line in open("../input/day22.txt")],[[],[]],0
for line in lines:
    if 'Player' in line: currentplayer=int(line[-2:-1])
    elif len(line)>0: cards[currentplayer-1].append(int(line))
print(calcscore(playgame(cards[0].copy(),cards[1].copy(),False)))
print(calcscore(playgame(cards[0],cards[1],True)))
