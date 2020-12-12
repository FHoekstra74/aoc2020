f=open('../input/day12.txt','r')
ship=[0,0]
way=[10,-1]
for l in f:
    i=l[0]
    i2=int(l[1:])
    if i == 'F':
        for j in range(2): ship[j]=ship[j]+(way[j] * i2) 
    elif i == 'N': way[1]-=i2
    elif i == 'E': way[0]+=i2
    elif i == 'S': way[1]+=i2
    elif i == 'W': way[0]-=i2
    else:
        for j in range(i2//90):
            temp=way[:]
            way[0]=temp[1]*-1 if i == 'R' else temp[1]
            way[1]=temp[0] if i == 'R' else temp[0]*-1
for j in range(2):
    if ship[j]<0:ship[j]*=-1
print (ship[0]+ship[1])
