def run(map,vectors,fourdimensions):
    l=list(map.keys())
    minx,miny,minz,minw,maxx,maxy,maxz,maxw=0,0,0,0,max(l)[0],max(l)[1],0,0
    for k in range(6):
        changes=[]
        for x in range(minx-k-1,maxx+k+2):
            for y in range(miny-k-1,maxy+k+2):
                for z in range(minz-k-1,maxz+k+2):
                    for w in range(minw-k-1 if fourdimensions else 0, maxw+k+2 if fourdimensions else 1):
                        n=0
                        for vector in vectors:
                            if (x+vector[0],y+vector[1],z+vector[2],w+vector[3]) in map: n+=1
                        if (x,y,z,w) in map: 
                            if not 2 <= n <= 3: changes.append(((x,y,z,w),0))
                        elif n==3: changes.append(((x,y,z,w),1))
        for change in changes:
            if change[1]==0: del map[change[0]]
            if change[1]==1: map[change[0]]=1
    return len(map)

f,map,vectors=open('../input/day17.txt','r'),{},[]
for y,l in enumerate(f):
    for x,c in enumerate(l.strip()):
        if c=='#': map[(int(x),int(y),0,0)]=1
for x in range(-1,2):
    for y in range(-1,2):
        for z in range(-1,2):
            for w in range(-1,2):
                if not(x==0 and y==0 and z==0 and w==0): vectors.append((x,y,z,w))
print(run(map.copy(),vectors,False))
print(run(map,vectors,True))
