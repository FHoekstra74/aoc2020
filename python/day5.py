def calc(boardingpass):
    rowstep,colstep,row,col=128,8,0,0
    for c in boardingpass:
        if c in ('F','B'): rowstep = rowstep // 2
        if c in ('L','R'): colstep = colstep // 2
        if c == 'B': row += rowstep
        if c == 'R': col += colstep
    return ((row * 8) + col)
seats=[calc(l.strip()) for l in open("../input/day5.txt","r")]
print(f"answera: {max(seats)}")
for seat in range(min(seats),max(seats)):
    if seat not in seats and seat+1 in seats and seat-1 in seats:
        print(f"answerb: {seat}")
