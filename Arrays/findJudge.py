# 997. Find the Town Judge
# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:

    # The town judge trusts nobody.
    # Everybody (except for the town judge) trusts the town judge.
    # There is exactly one person that satisfies properties 1 and 2.

# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        h, p = {}, set()
        if not trust:
            return N
        for i in range(len(trust)):
            if trust[i][1] in h:
                h[trust[i][1]].append(trust[i][0])
                p.add(trust[i][0])
            else:
                h[trust[i][1]] = [trust[i][0]]
                p.add(trust[i][0])
        if len(p) == N:
            return -1
        for k,val in h.items():
            if len(val) == N-1 and k not in p:
                return k
        return -1
        
def findJudge(self, N: int, trust: List[List[int]]) -> int:
    
    if len(trust) < N - 1:
        return -1
    
    indegree = [0] * (N + 1)
    outdegree = [0] * (N + 1)
    
    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1
        
    for i in range(1, N + 1):
        if indegree[i] == N - 1 and outdegree[i] == 0:
            return i
    return -1
    
def findJudge(self, N: int, trust: List[List[int]]) -> int:

    if len(trust) < N - 1:
        return -1

    trust_scores = [0] * (N + 1)

    for a, b in trust:
        trust_scores[a] -= 1
        trust_scores[b] += 1
    
    for i, score in enumerate(trust_scores[1:], 1):
        if score == N - 1:
            return i
    return -1
    
    
