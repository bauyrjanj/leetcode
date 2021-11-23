import sys
from collections import defaultdict
def oab(transactions):
    debts = defaultdict(int)
    for f, t, amount in transactions:
        debts[f]-=amount
        debts[t]+=amount
    debts_list = [debts[id] for id in debts if debts[id]]
    n = len(debts_list)
    def dfs(idx):
        while idx<n and debts_list[idx]==0:
            idx+=1

        if idx==n:
            return 0

        ans = sys.maxsize

        for i in range(idx+1, n):
            if debts_list[idx]*debts_list[i]<0:
                debts_list[i]+=debts_list[idx]
                ans=min(ans, dfs(idx+1)+1)
                debts_list[i]-=debts_list[idx]
        return ans

    return dfs(0)

if __name__=="__main__":
    # transactions = [[0,1,10], [2,0,5]]
    # transactions = [[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]
    # transactions = [[0, 1, 2], [1, 2, 1], [1, 3, 1]]
    # transactions = [[0,1,5],[2,3,1],[2,0,1],[4,0,2]]
    transactions = [[2,0,5],[3,4,4]]
    print(oab(transactions))

