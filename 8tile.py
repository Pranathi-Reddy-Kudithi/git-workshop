'''import heapq
class PuzzleState:
    def __init__(self, board, parent, move, depth, cost):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
    def __lt__(self, other):
        return self.cost < other.cost
def print_board(board):
    for row in range(0, 9, 3):
        row_visual = ""
        for tile in board[row:row + 3]:
            if tile == 0:
                row_visual += '   '
            else:
                row_visual +=f' {tile} '
        print(row_visual)
moves = {'U': -3,'D': 3,'L': -1,'R': 1}
def heuristic(board,goal):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(goal[i], 3)
            x2, y2 = divmod(board[i], 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def move_tile(board, move, blank_pos):
    new_board = board[:]
    new_blank_pos = blank_pos + moves[move]
    new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
    return new_board
def a_star(start_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, PuzzleState(start_state, None, None, 0, heuristic(start_state,goal_state)))
    while open_list:
        current_state = heapq.heappop(open_list)
        if current_state.board == goal_state:
            return current_state
        closed_list.add(tuple(current_state.board))
        blank_pos = current_state.board.index(0)
        for move in moves:
            if move == 'U' and blank_pos < 3:
                continue
            if move == 'D' and blank_pos > 5:
                continue
            if move == 'L' and blank_pos % 3 == 0:
                continue
            if move == 'R' and blank_pos % 3 == 2:
                continue
            new_board = move_tile(current_state.board, move, blank_pos)
            if tuple(new_board) in closed_list:
                continue
            new_state = PuzzleState(new_board, current_state, move, current_state.depth + 1, current_state.depth + 1 + heuristic(new_board,goal_state))
            heapq.heappush(open_list, new_state)
    return None
def print_solution(solution):
    path = []
    current = solution
    while current:
        path.append(current)
        current = current.parent
    path.reverse()
    for step in path:
        print(f"Move: {step.move}")
        print_board(step.board)
initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]
goal_state = [1, 2, 0, 3, 4, 5, 6, 7, 8]
solution = a_star(initial_state)
if solution:
    print_solution(solution)
else:
    print("No solution found")'''

import heapq

moves = {'U': -3, 'D': 3, 'L': -1, 'R': 1}
goal = [1, 2, 0, 3, 4, 5, 6, 7, 8]

class State:
    def __init__(s, b, p, m, d): s.b, s.p, s.m, s.d = b, p, m, d
    def __lt__(s, o): return (s.d + h(s.b)) < (o.d + h(o.b))

def h(b):  # Manhattan distance
    return sum(abs(i // 3 - b[i] // 3) + abs(i % 3 - b[i] % 3) for i in range(9) if b[i])

def move(b, m, z): 
    nb = b[:]
    nz = z + moves[m]
    nb[z], nb[nz] = nb[nz], nb[z]
    return nb

def solve(start):
    q, seen = [State(start, None, None, 0)], set()
    while q:
        s = heapq.heappop(q)
        if s.b == goal: return s
        seen.add(tuple(s.b))
        z = s.b.index(0)
        for m in moves:
            if (m == 'U' and z < 3) or (m == 'D' and z > 5) or (m == 'L' and z % 3 == 0) or (m == 'R' and z % 3 == 2): continue
            nb = move(s.b, m, z)
            if tuple(nb) not in seen: heapq.heappush(q, State(nb, s, m, s.d + 1))

def show(s):
    path = []
    while s: path.append(s); s = s.p
    for step in reversed(path):
        print(f"Move: {step.m}")
        for i in range(0, 9, 3): print(' '.join(f'{x or " "}' for x in step.b[i:i+3]))
        print()

initial = [1, 2, 3, 4, 5, 6, 0, 7, 8]
res = solve(initial)
show(res) if res else print("No solution")

