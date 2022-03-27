class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        noofsold,rt=[],[]
        for i in mat:
            noofsold.append(sum(i))
        test=noofsold[:]
        while len(rt)!=len(noofsold):
            mi=min(test)
            for i in range(0,len(noofsold)):
                if noofsold[i]==mi:
                    if i not in rt:
                        rt.append(i)
                        break
            test.remove(mi)
        return rt[:k]