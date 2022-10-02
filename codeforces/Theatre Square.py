from math import ceil

n, m, a = map(int, input().split())

global nDimensionCount
global mDimensionCount
if n < a < m:
    nDimensionCount = 1
    mDimensionCount = ceil(m / a)
if m < a < n:
    mDimensionCount = 1
    nDimensionCount = ceil(n / a)
else:
    nDimensionCount = ceil(n / a)
    mDimensionCount = ceil(m / a)
print(nDimensionCount * mDimensionCount)
