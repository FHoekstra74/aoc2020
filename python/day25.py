f = open('../input/day25.txt', 'r')
cardkey = int(f.readline().strip())
doorkey = int(f.readline().strip())
loops, startval = 0, 1
while startval != cardkey:
    startval = (startval * 7) % 20201227
    loops += 1
startval = 1
for i  in range(loops): startval = (startval * doorkey) % 20201227
print(startval)
