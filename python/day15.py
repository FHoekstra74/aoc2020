input,speak,history,previous=[0,1,5,10,3,12,19],0,{},0
for i in range(30000000):
    if i<len(input): speak=input[i]
    else:
        if previous in history: speak=i-history[previous]
        else: speak=0
    if i>0: history[previous]=i
    if i+1==2020: print(f"a:{speak}")
    previous=speak
print(f"b:{speak}")
