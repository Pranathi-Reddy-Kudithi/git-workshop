import re
code=[]
while True:
    line=input()
    if not line:
        break
    code.append(line)
reg_map={}
r=1
out=[]
for line in code:
    lhs,rhs=line.split("=",1)
    lhs=lhs.strip()
    rhs=rhs.strip()
    parts=re.findall(r'\w+|[\+\-\*/]',rhs)
    if len(parts)==1:
        op1=parts[0]
        src=reg_map.get(op1,op1)
        if lhs.startswith("t"):
            reg=f"R{r}"
            reg_map[lhs]=reg
            out.append(f"MOV {reg},{src}")
            r+=1
        else:
            out.append(f"MOV {lhs},{src}")
    else:
        x,op,y=parts
        reg=f"R{r}"
        r+=1
        reg_map[lhs]=reg
        src1=reg_map.get(x,x)
        src2=reg_map.get(y,y)
        ops = {'+':'ADD','-':'SUB','*':'MUL','/':'DIV'}
        out.append(f"{ops[op]} {reg},{src1},{src2}")
        r+=1
print("\n".join(out))
