c=1
def g(e):
    global c
    e=e.strip()
    if e.isalnum():
        return e
    for o in "+-*/":
        d=0
        for i in range(len(e)-1,-1,-1):
            if e[i]=="(":
                d+=1
            elif e[i]==")":
                d-=1
            elif d==0 and e[i]==o:
                l,r=g(e[:i]),g(e[i+1:])
                t=f"t{c}"
                print(f"{t}={l} {o} {r}")
                c+=1
                return t
    return g(e[1:-1])
x,y=input().split("=",1)
print(f"{x}={g(y)}")


               


'''def g(e):
    global c
    e = e.strip()
    if not e:
        raise ValueError("Invalid expression: Empty part detected")   # Better message
    if e.isalnum():
        return e
    for o in "+-*/":
        d = 0
        for i in range(len(e)-1, -1, -1):
            if e[i] == "(":
                d += 1
            elif e[i] == ")":
                d -= 1
            elif d == 0 and e[i] == o:
                left = e[:i].strip()
                right = e[i+1:].strip()
                # Check if left or right is empty
                if not left or not right:
                    raise ValueError(f"Invalid expression near operator '{o}' in: {e}")
                l, r = g(left), g(right)
                t = f"t{c}"
                print(f"{t}={l} {o} {r}")
                c += 1
                return t
    if e[0] == "(" and e[-1] == ")":
        return g(e[1:-1].strip())
    raise ValueError(f"Invalid expression: {e}")
x, y = input().split("=", 1)
y = y.strip().rstrip(";")
print(f"{x}={g(y)}")
'''
