class MapColoring:
    def __init__(self,states,neighbors,colors):
        self.states = states
        self.neighbors = neighbors
        self.colors = colors
        self.colored={}
    def is_valid(self,state,color):
        for neighbor in self.neighbors.get(state,[]):
            if neighbor in self.colored and self.colored[neighbor]==color:
                return False
        return True
    def select_uncolor(self):
        for state in self.states:
            if state not in self.colored:
                return state
        return None
    def color_csp(self):
        if len(self.colored)==len(self.states):
            return self.colored
        state = self.select_uncolor()
        for color in self.colors:
            if self.is_valid(state,color):
                self.colored[state]=color
                result = self.color_csp()
                if result is not None:
                    return result
                del self.colored[state]
        return None
states = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []  # Tasmania has no neighbors
}
colors = ["Red", "Green", "Blue","Yellow"]
csp=MapColoring(states,neighbors,colors)
solution=csp.color_csp()
if solution is not None:
    print("SOLUTION IS FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    for state, color in solution.items():
        print(f"{state}->{color}")
    print("\n")
else:
    print("NO SOLUTION FOUND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
