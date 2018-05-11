import random


class MarcovChainGenerator:
    def __init__(self):
        self.last = None
        self.counter = 0
        self.transitions = dict() # State -> State -> Int
        self.inputFoo = lambda x: x
        self.outputFoo = lambda x: x
        self.actualState = None
        self.startState = None

    def setInput(self, fun):
        self.inputFoo = fun

    def setOutput(self, fun):
        self.outputFoo = fun

    def addNext(self, nxtt):
        nxt = self.inputFoo(nxtt)
        if self.counter == 0:
            self.last = nxt
        else:
            if self.last in self.transitions.keys():
                if nxt in self.transitions[self.last]:
                    self.transitions[self.last][nxt] += 1
                else:
                    self.transitions[self.last][nxt] = 1
            else:
                self.transitions[self.last] = dict()
                self.transitions[self.last][nxt] = 1
        self.last = nxt
        self.counter += 1

    def setState(self, state):
        self.actualState = state
        self.startState = state

    def getNextState(self):
        if self.actualState in self.transitions.keys():
            s = sum(self.transitions[self.actualState].values(), 0)
            rand = random.randrange (0, s)
            print("For state", self.actualState, "we have sum of", s)
            for state in self.transitions[self.actualState]:
                val = self.transitions[self.actualState][state]
                if rand - val < 0:
                    self.actualState = state
                    return state
                else:
                    rand -= val
        self.actualState = self.startState
        return self.actualState

generator = MarcovChainGenerator()
for l in "to jest przykladowy test zobaczymy co tu sie dziejeee kekeke":
    generator.addNext(l)

print(generator.transitions)
generator.setState('a')
st = ""
for i in range(20):
    st += generator.getNextState()

print(st)
