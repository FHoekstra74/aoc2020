f=open('../input/day12.txt','r')
d='E'
ship=[0,0]
for l in f:
    i=l[0]
    i2=int(l[1:])
    if i == 'F':
        if d=='E':ship[0]+=i2
        elif d =='S':ship[1]+=i2
        elif d =='W':ship[0]-=i2
        else: ship[1]-=i2
    elif i == 'N': ship[1]-=i2 
    elif i == 'E': ship[0]+=i2
    elif i == 'S': ship[1]+=i2
    elif i == 'W': ship[0]-=i2
    else:
        for j in range(i2//90):
            if d=='E': d='S' if i =='R' else 'N'
            elif d=='S': d='W' if i =='R' else 'E'
            elif d=='W': d='N' if i =='R' else 'S'
            elif d=='N': d='E' if i =='R' else 'W'
  #  elif i == 'R':
  #      for j in range(i2//90):
  #          if d=='E': d='S'
  #          elif d=='S': d='W'
  #          elif d=='W': d='N'
  #          elif d=='N' : d='E'
  #  elif i == 'L':
  #      for j in range(i2//90):
  #          if d=='E': d='N'
  #          elif d=='N': d='W'
  #          elif d=='W': d='S'
  #          elif d=='S' : d='E'
for j in range(2):
    if ship[j]<0:ship[j]*=-1
print(ship[0]+ship[1])
