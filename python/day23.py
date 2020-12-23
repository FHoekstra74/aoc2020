class cup: 
    __slots__=['value','next']
    def __init__(self, value): self.value = value

def run (input,runs,circlelength):
    prev, current = None, None
    cups = [None] * (circlelength + 1)
    for i in range(circlelength):
        newcup = cup(input[i]) if i<len(input) else cup(i + 1)
        cups[newcup.value] = newcup
        if prev: prev.next = newcup
        prev = newcup
    prev.next = cups[input[0]]
    for i in range(runs):
        current = current.next if current else cups[input[0]]
        picks = [current.next, current.next.next, current.next.next.next]
        current.next = picks[-1].next
        destval = circlelength if current.value == 1 else current.value - 1
        while destval in [i.value for i in picks]: destval = circlelength if destval == 1 else destval - 1
        dest = cups[destval]
        picks[-1].next = dest.next
        dest.next = picks[0]
    return cups[1]

input, answera = [int(i) for i in '784235916'], ''
result=run(input.copy(),100,len(input))
for j in range(len(input)-1):
    result = result.next
    answera += str(result.value)
print(f"a: {answera}")
result = run(input,10000000,1000000)
print(f"b: {result.next.value * result.next.next.value}")
