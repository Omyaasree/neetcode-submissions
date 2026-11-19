class MinStack:

    def __init__(self):
        self.ostack = []
        self.mstack = []

    def push(self, val: int) -> None:
        if not self.ostack:
            self.ostack.append(val)
            self.mstack.append(val)
        else: 
            self.ostack.append(val) 
            self.mstack.append(min(self.mstack[-1],val))

    def pop(self) -> None:
        self.ostack.pop()
        self.mstack.pop()

    def top(self) -> int:
        return self.ostack[-1]

    def getMin(self) -> int:
        return self.mstack[-1]


        
