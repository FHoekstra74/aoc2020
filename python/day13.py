lines=[line.strip() for line in open("../input/day13.txt","r")]
busses,ts,result = [int(l) if l != "x" else -1 for l in lines[1].split(",")],int(lines[0]),{}
for bus in [bus for bus in busses if bus > 0]:
    test = (ts // bus -1) * bus
    while test < ts:
        test += bus
        if test >= ts: result[test] = bus
lowest = sorted(result)[0]
print(f"a:{(lowest-ts)*result[lowest]}")

ts,stop,ok=1,False,set()
while not stop:
    tmp = 1
    for bus in ok: tmp *= bus
    ts += tmp
    stop = True
    for i,bus in enumerate(busses):
        if bus > 0:
            if (ts+i) % bus != 0: stop = False
            else: 
                if not bus in ok: ok.add(bus)
print(f"b:{ts}")
