def traverse(coor,xstep,ystep,maxx,maxy):
    val,xpos,ypos=0,0,0
    while ypos<maxy:
        if (xpos,ypos) in coor: val+=1
        ypos+=ystep
        if xpos>(maxx-xstep): xpos=0-(maxx-xpos+1)
        xpos+=xstep
    return val

f,y,coor = open("../input/day3.txt", "r"),0,[]
for l in f:
    x=0
    for c in l.strip():
        if c == '#': coor.append((x,y))
        x+=1
    y+=1
print(traverse(coor,3,1,x-1,y))
print(traverse(coor,1,1,x-1,y) * traverse(coor,3,1,x-1,y) * traverse(coor,5,1,x-1,y) * traverse(coor,7,1,x-1,y) * traverse(coor,1,2,x-1,y))
