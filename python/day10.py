lines=[int(line.strip()) for line in open ('../input/day10.txt','r')]
lines.append(0)
lines.append(max(lines)+3)
lines.sort()
diffs={1:0,2:0,3:0}
for cnt,adapter in enumerate(lines):
    if cnt>0: diffs[adapter-lines[cnt-1]]+=1
print(f"a:{diffs[1] * (diffs[3])}")

ways=dict.fromkeys(lines,0)
ways[max(lines)+3]=1
lines.reverse()
for adapter in lines:
  for i in range(1,4): 
      if adapter+i in ways: ways[adapter]+=ways[adapter+i]
print(f"b:{ways[0]}")
