import math
def printtile(tile):
    for l in tile:
        print(l)

def rotateright(tile):
    newtile=[]
    newline=''
    for x in range(len(tile[0])):
        newline=''
        for y in range(len(tile[0])):
            newline+=tile[len(tile[0])-y-1][x]
        newtile.append(newline)
    return newtile

def flip(tile):
    newtile=[]
    for line in tile: newtile.append(line[::-1])
    return newtile

def rightedge(tile):
    s=''
    for i in range(len(tile)):
        s+=tile[i][-1]
    return s

def leftedge(tile):
    s=''
    for i in range(len(tile)):
        s+=tile[i][0]
    return s

def topedge(tile):
    return(tile[0])

def bottomedge(tile):
    return(tile[-1])

f=open('../input/day20.txt','r')
tileedges={}
tiles={}
tileid=0
for line in f:
    line=line.strip()
    if 'Tile' in line:
        tileid=int(line.split(' ')[1].replace(':',''))
        tile=[]
    elif len(line) > 0:
        tile.append(line.strip())
    else:
        edges=[]
        edges.append(topedge(tile))
        edges.append(bottomedge(tile))
        edges.append(leftedge(tile))
        edges.append(rightedge(tile))
        edges.append(topedge(tile)[::-1])
        edges.append(bottomedge(tile)[::-1])
        edges.append(leftedge(tile)[::-1])
        edges.append(rightedge(tile)[::-1])
        tileedges[tileid]=edges
        tiles[tileid]=tile
alledges=[]
for edges in tileedges.values():
    for edge in edges: alledges.append(edge)

firstcornertile=0
answera=1
for tileid,edges in tileedges.items():
    uniqueedge=0
    for edge in edges:
        if alledges.count(edge) == 1: uniqueedge+=1
    if uniqueedge==4:
        if firstcornertile==0: firstcornertile=tileid
        answera*=tileid

print(answera)

lefttoptile=tiles[firstcornertile]
lefttopedges=[]
for edge in tileedges[firstcornertile]:
    if alledges.count(edge) == 1: lefttopedges.append(edge)

for i in range(4):
    if topedge(lefttoptile) in lefttopedges and leftedge(lefttoptile) in lefttopedges:
        break
    else:
        lefttoptile=rotateright(lefttoptile)

alltiles={}
alltiles[(0,0)]=lefttoptile
usedtiles=[firstcornertile]
max=int(math.sqrt(len(tiles)))
for y in range(max):
    for x in range(max):
        if x==0 and y==0: pass
        else:
            if x > 0:
                newtileid=0
                if (x-1,y) in alltiles:
                    edge=rightedge( alltiles[(x-1,y)])
                    for tileid,edges in tileedges.items():
                        if edge in edges and tileid not in usedtiles:
                            newtileid = tileid
                    newtile=tiles[newtileid]
                    for i in range(9):
                        if leftedge(newtile) == edge:
                            usedtiles.append(newtileid)
                            alltiles[x,y]=newtile
                            break
                        else:
                            if i==4: newtile=flip(newtile)
                            else: newtile=rotateright(newtile)
            else:
                newtileid=0
                if (x,y-1) in alltiles:
                    edge=bottomedge(alltiles[x,y-1])
                    for tileid,edges in tileedges.items():
                        if edge in edges and tileid not in usedtiles:
                            newtileid = tileid
                    newtile=tiles[newtileid]
                    for i in range(9):
                        if topedge(newtile) == edge:
                            usedtiles.append(newtileid)
                            alltiles[x,y]=newtile
                            break
                        else:
                            if i==4: newtile=flip(newtile)
                            else: newtile=rotateright(newtile)

y=0
n=0
bigtile=[]
for row in range(max * len(lefttoptile)):
    newline=''
    for x in range(max):
        newline+=alltiles[(x,y)][n][1:-1]
    if n>0 and (n+1)<len(lefttoptile):
        bigtile.append(newline)
    n+=1
    if n==len(lefttoptile):
        n=0
        y+=1

monster = []
monster.append('                  # ')
monster.append('#    ##    ##    ###')
monster.append(' #  #  #  #  #  #   ')
found=False
f=0
while not found:
    for i in range(len(bigtile)-len(monster)):
        for j in range(len(bigtile)-len(monster[0])):
            ok=0
            for k in range(len(monster)):
                for l in range(len(monster[0])):
                    if monster[k][l] == '#' and bigtile[i+k][j+l] == '#':
                        ok+=1
            if ok==15:
                for k in range(len(monster)):
                    for l in range(len(monster[0])):
                        if monster[k][l] == '#' and bigtile[i+k][j+l] == '#':
                            oldstr=bigtile[i+k]
                            pos=j+l
                            oldstr = oldstr[:pos] + 'O' + oldstr[pos + 1:]
                            bigtile[i+k]=oldstr
                found=True
    if not found:
        if f==4:
            bigtile=flip(bigtile)
        else:
            bigtile=rotateright(bigtile)
        f+=1
#printtile(bigtile)

answerb=0
for i in range(len(bigtile)):
    for j in range(len(bigtile)):
        if bigtile[i][j]=='#': answerb+=1
print(answerb)
