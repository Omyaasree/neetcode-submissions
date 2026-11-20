class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) == len(t):    

            hashs = {}
            for i in s:
                if i in hashs:
                    hashs[i] += 1
                else :
                    hashs[i] = 1
            sorts = dict(sorted(hashs.items()))

            hasht = {}
            for i in t:
                if i in hasht:
                    hasht[i] += 1
                else :
                    hasht[i] = 1
            sortt = dict(sorted(hasht.items()))

            keyss = list(sorts.keys())
            values = list(sorts.values())

            keyt = list(sortt.keys())
            valuet = list(sortt.values())

            for i in range(len(keyss)):
                print(keyss[i] + " , " + keyt[i])
                if keyss[i] != keyt[i]:
                    return False
                else :
                    if values[i] != valuet[i]:
                        return False
            return True
            
        return False



            

        


        