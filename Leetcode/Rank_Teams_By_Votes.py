class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        for x in votes:
            for i in range(len(x)):
                if x[i] not in d:
                    d[x[i]] = [0]*len(x)
                d[x[i]][i] += 1
        l = sorted(list(d.keys())) # sort the team alphabetically first       
        ans = sorted(l, key = lambda x: d[x], reverse = True) # then sort it based on votes
        return "".join(ans)