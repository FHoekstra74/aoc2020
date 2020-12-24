def calcpos(line):
    i, pos = 0, (0, 0)
    while i < len(line):
        if line[i] in ('e', 'w'): instr = line[i:i + 1]
        else: instr = line[i:i + 2]
        if instr == 'e': pos = (pos[0] + 2, pos[1])
        elif instr == 'se': pos = (pos[0] + 1, pos[1] + 1)
        elif instr == 'sw': pos = (pos[0] - 1, pos[1] + 1)
        elif instr == 'w': pos = (pos[0] - 2, pos[1])
        elif instr == 'nw': pos = (pos[0] - 1, pos[1] - 1)
        elif instr == 'ne': pos = (pos[0] + 1, pos[1] - 1)
        i += len(instr)
    return pos

map, vectors, changes = set(), ((2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)), []
for tile in [calcpos(line.strip()) for line in open('../input/day24.txt', 'r') if len(line.strip()) > 0]:
    if tile in map: map.remove(tile)
    else: map.add(tile)
print(f"a: {len(map)}")
for _ in range(100):
    for x in range(min([i[0] for i in map]) - 2, max([i[0] for i in map]) + 3):
        for y in range(min([i[1] for i in map]) - 1, max([i[1] for i in map]) + 2):
            cnt, black = 0, (x, y) in map
            for vector in vectors:
                if (x + vector[0], y + vector[1]) in map: cnt += 1
            if black and (cnt == 0 or cnt > 2): changes.append((x, y, False))
            if not black and cnt == 2: changes.append((x, y, True))
    for change in changes:
        if change[2]: map.add((change[0], change[1]))
        elif (change[0], change[1]) in map: map.remove((change[0], change[1]))
print(f"b: {len(map)}")
