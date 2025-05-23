from math import inf

def minimax(d, i, maxP, vals, a, b):
    if d == 3:
        return vals[i]

    best = -inf if maxP else inf
    for j in range(2):
        child = i * 2 + j
        role = "maximizing" if maxP else "minimizing"
        print(f"Depth {d}: {role}, before evaluating child {child}, alpha={a}, beta={b}")
        val = minimax(d + 1, child, not maxP, vals, a, b)

        if maxP:
            best = max(best, val)
            a = max(a, best)
        else:
            best = min(best, val)
            b = min(b, best)

        print(f"Depth {d}: {role}, after evaluating child {child}, best={best}, alpha={a}" if maxP else f"Depth {d}: {role}, after evaluating child {child}, best={best}, beta={b}")
        
        if b <= a:
            print(f"Depth {d}: Pruning at node {i} because beta <= alpha ({b} <= {a})")
            break
    return best

values = [4, 6, 1, 10, 7, 9, 33, 21]
print("The optimal value is:", minimax(0, 0, True, values, -inf, inf))
