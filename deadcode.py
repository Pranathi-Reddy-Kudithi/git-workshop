

def is_used(var, code_lines):
    for line in code_lines:
        if line is None:
            continue
        if var in line and not line.strip().startswith(var + " ="):
            return True
    return False

def eliminate_redundant_subexpressions(lines):
    optimized = []
    expr_map = {}

    for line in lines:
        if '=' not in line:
            optimized.append(line)
            continue

        var, expr = map(str.strip, line.split('=', 1))

        if expr in expr_map:
            optimized.append(f"{var} = {expr_map[expr]}")
        else:
            optimized.append(f"{var} = {expr}")
            expr_map[expr] = var

    return optimized

def eliminate_dead_code(lines):
    used_vars = set()
    cleaned_lines = lines[:]  # Make a copy to avoid modifying while iterating

    for i in range(len(cleaned_lines) - 1, -1, -1):
        line = cleaned_lines[i]
        if line is None:
            continue
        if '=' in line:
            var, _ = map(str.strip, line.split('=', 1))
            if var in used_vars:
                continue
            if is_used(var, cleaned_lines[i+1:]):
                used_vars.add(var)
            else:
                cleaned_lines[i] = None  # Mark for deletion
        else:
            for token in line.strip().split():
                if token.isidentifier():
                    used_vars.add(token)

    return [line for line in cleaned_lines if line is not None]

# === Sample Input Code ===
input_code = """
a = 5
b = 10
c = a + b
d = a + b
e = c * 2
f = e + 5
x = 99
y = x + 1
z = e - a
temp = 42
print(z)
"""

print("Original Code:")
print(input_code.strip())

# Step 1: Split into lines
lines = input_code.strip().split('\n')

# Step 2: Redundant Subexpression Elimination
rse_lines = eliminate_redundant_subexpressions(lines)
print("\nAfter Redundant Subexpression Elimination:")
print('\n'.join(rse_lines))

# Step 3: Dead Code Elimination
final_lines = eliminate_dead_code(rse_lines)
print("\nAfter Dead Code Elimination:")
print('\n'.join(final_lines))

