import io, os, sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_right
INF = float('inf')
def lis(nums):
    dp = [INF] * (len(nums) + 1);dp[0] = -INF
    for num in nums:
        j = bisect_right(dp, num)
        if dp[j - 1] <= num < dp[j]:dp[j] = num
    for i, v in enumerate(dp):
        if v < INF:res = i
    return res
def solve(N, K, nums):
    count = [0] * (N + 1);cands = [];res = [-1] * N
    for num in nums:count[num] += 1
    for num, cnt in enumerate(count):
        if cnt > K: return [-1]
        cands += [num] * cnt
    for i in range(N):
        for j, cand in enumerate(cands):
            hi = lis(res[:i] + [cand] + cands[:j] + cands[j + 1:])
            lo = lis(res[:i] + [cand] + cands[j + 1:][::-1] + cands[:j][::-1])
            if lo <= K <= hi:res[i] = cand;cands = cands[:j] + cands[j + 1:];break
    return res
for _ in range(int(input())):N, K = list(map(int, input().split()));nums = list(map(int, input().split()));out = solve(N, K, nums);print(' '.join(map(str, out)))