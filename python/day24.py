def calcpos(line):
    instructions, pos, i = {'e':(2, 0), 'se':(1, 1), 'sw':(-1, 1), 'w':(-2, 0), 'nw':(-1, -1), 'ne':(1, -1)}, (0, 0), 0
    while i < len(line):
        if line[i] in ('e', 'w'): instr = line[i:i + 1]
        else: instr = line[i:i + 2]
        pos = (pos[0] + instructions[instr][0], pos[1] + instructions[instr][1])
        i += len(instr)
    return pos

map, vectors = set(), ((2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1))
for tile in [calcpos(line.strip()) for line in open('../input/day24.txt', 'r') if len(line.strip()) > 0]:
    if tile in map: map.remove(tile)
    else: map.add(tile)
print(f"a: {len(map)}")
for _ in range(100):
    new = map.copy()
    for x in range(min([i[0] for i in map]) - 2, max([i[0] for i in map]) + 3):
        for y in range(min([i[1] for i in map]) - 1, max([i[1] for i in map]) + 2):
            cnt, black = sum([1 if (x + vector[0], y + vector[1]) in map else 0 for vector in vectors]), (x, y) in map
            if black and (cnt == 0 or cnt > 2): new.remove((x, y))
            if not black and cnt == 2: new.add((x, y))
    map = new                
print(f"b: {len(map)}")
