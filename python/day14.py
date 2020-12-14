f,mema,memb,mask=open('../input/day14.txt','r'),{},{},[]
for line in f:
    l=line.split('=')
    instr,para=l[0].strip(),l[1].strip()
    if 'mask' in instr: mask = [x for x in para]
    elif 'mem' in instr:
        val = f"{bin(int(para))[2:]:0>36}"
        newval=([mask[i] if itm != 'X' else val[i] for i,itm in enumerate(mask)] )
        mema[instr[4:-1]]=int(''.join(newval),2)

        addr,memaddr,combis=f"{bin(int(instr[4:-1]))[2:]:0>36}",[],[]
        for i,itm in enumerate(mask):
            if itm=='X': memaddr.append('X')
            elif itm=='1': memaddr.append('1')
            elif itm=='0': memaddr.append(addr[i])
        combis.append(memaddr)
        for _ in range (combis[0].count('X')):
            for entry in combis.copy():
                first,second=entry.copy(),entry.copy()
                pos=entry.index('X')
                first[pos],second[pos]='0','1'
                combis.remove(entry)
                combis.append(first)
                combis.append(second)
        for addr in combis: memb[int(''.join(addr),2)]=int(para)
print(f"a:{sum(mema.values())}")
print(f"b:{sum(memb.values())}")