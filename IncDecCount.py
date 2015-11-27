#given a set of n numbers l, and a window of size k, 
#calculate the difference in increasing subranges and
#decreasing subranges in each window k. 

n, k = raw_input().split()
l = map(int, raw_input().split())

n = int(n)
k = int(k)

leftInc, leftDec, rightDec, rightInc = (range(n) for i in range(4))

# swap until each element has right-most/leftmost increasing/decreasing indices
for i in range(n):
    if i > 0:
        if l[i] >= l[i-1]:
            leftInc[i] = leftInc[i-1]
        if l[i] <= l[i-1]:
            leftDec[i] = leftDec[i-1]
    m = n-i-1
    if (m < n-1):
        if l[m] <= l[m+1]:
            rightInc[m] = rightInc[m+1]
        if l[m] >= l[m+1]:
            rightDec[m] = rightDec[m+1]
S = 0
for i in range(n):
    lInc = max(leftInc[i], i-k)  # max check to maintain window size limit
    lDec = max(leftDec[i], i-k)
    S += (i-lInc)   # increment sum by distance of added non-increasing element
    S -= (i-lDec)   # decrement sum by distance of added non-decreasing element
    if i-k >= 0:
        rInc = min(rightInc[i-k], i)
        rDec = min(rightDec[i-k], i)
        S -= rInc-(i-k)
        S += rDec-(i-k)
    if i-k+1 >= 0:
        print S

