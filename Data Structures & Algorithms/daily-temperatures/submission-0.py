class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        stack = []
        dstack = []

        for temp in temperatures:
            stack.append(temp)
            dstack.append(temp)

        for i in range(len(stack)):
            count = 0
            warmer = False 
            
            for j in range(i + 1, len(stack)):
                count += 1 
                
                if stack[j] > stack[i]:
                    warmer = True
                    break 
            
            if not warmer:
                count = 0
                
            dstack[i] = count

        dstack[len(dstack) - 1] = 0

        print(stack)
        print(dstack)

        return dstack