def countocc(map,x,y,insight):
    cnt,vectors=0,[(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
    for vector in vectors:
        dx,dy,found=vector[0],vector[1],False if insight else True
        while not found:
            if (x+dx,y+dy) in map and map[x+dx,y+dy] == '.':
                if dx<0: dx-=1
                if dx>0: dx+=1
                if dy<0: dy-=1
                if dy>0: dy+=1
            else: found=True
        if (x+dx,y+dy) in map and map[(x+dx,y+dy)]=='#': cnt+=1
    return cnt

def calc(map,insight,occcount):
    maxx,maxy,changes=max(map)[0],max(map)[1],['dummy']
    while len(changes)>0:
        changes=[]
        for x in range(maxx+1):
            for y in range(maxy+1):
                if map[(x,y)] != '.':
                    if map[(x,y)] == 'L':
                        if countocc(map,x,y,insight) == 0: changes.append((x,y,'#'))
                    elif map[(x,y)] == '#':
                        if countocc(map,x,y,insight) >= occcount: changes.append((x,y,'L'))
        for change in changes: map[change[0],change[1]]=change[2]
    return len([val for val in map.values() if val == '#'])

f,map=open('../input/day11.txt','r'),{}
for y,l in enumerate(f):
    for x,c in enumerate(l.strip()):
        map[(x,y)]=c
print(calc(map.copy(),False, 4))
print(calc(map,True, 5))
