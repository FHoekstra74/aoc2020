def calc(boardingpass):
    rows,cols,rowmin,rowmax,colmin,colmax=128,8,0,127,0,7
    for c in boardingpass:
        if c in ('F','B'): rows = rows // 2
        if c in ('L','R'): cols = cols // 2
        if c == 'F': rowmax = rowmax - rows
        if c == 'B': rowmin = rowmin + rows
        if c == 'L': colmax = colmax - cols
        if c == 'R': colmin = colmin + cols
    return ((rowmax * 8) + colmax)
seats,f=[],open("../input/day5.txt","r")
for l in f: seats.append(calc(l.strip()))
print(f"answera: {max(seats)}")
for seat in range(0,128*8):
    if seat not in seats and seat+1 in seats and seat-1 in seats:
        print(f"answerb: {seat}")
