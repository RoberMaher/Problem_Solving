# B. Everything Everywhere
# time limit per test1.5 seconds
# memory limit per test256 megabytes

# An array is called good if the difference between the maximum value and the minimum value in the array is equal to the greatest common divisor (GCD) of all the elements in the array. Note that an empty array is considered to be not good.

# More formally, an array [a1,a2,…,am]
#  is good if and only if
# max(a1,a2,…,am)−min(a1,a2,…,am)=gcd(a1,a2,…,am).

# You are given a permutation∗
#  p
#  of length n
# . Determine the number of good subarrays†
#  in the given permutation.

# ∗
# A permutation of length m
#  is an array consisting of m
#  distinct integers from 1
#  to m
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (m=3
#  but there is 4
#  in the array).

# †
# An array b
#  is a subarray of an array a
#  if b
#  can be obtained from a
#  by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end. In particular, an array is a subarray of itself.

# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.

# The first line of each testcase contains a single integer n
#  (2≤n≤2⋅105
# ) — the length of the permutation p
# .

# The second line of each testcase contains n
#  integers p1,p2,…,pn
#  (1≤pi≤n
# ) — the permutation p
# . It is guaranteed that p
#  is a permutation.

# It is guaranteed that the sum of n
#  over all the test cases does not exceed 2⋅105
# .

# Output
# For each testcase, print a single integer — the number of good subarrays in the given permutation.

# Example
# InputCopy
# 3
# 2
# 1 2
# 9
# 6 1 5 9 4 7 2 8 3
# 4
# 1 2 3 4
# OutputCopy
# 1
# 0
# 3
# Note
# For the first testcase, only one subarray is good, which is [1,2]
# .

# For the second testcase, it can be proven that no good subarrays exist in the given permutation.

import sys
import math

def solve():
    input = sys.stdin.readline
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        
        count = 0
        
        # Try each possible starting index
        i = 0
        while i < n:
            # For each start, track min, max, gcd, and when we get third distinct value
            mn = mx = p[i]
            g = 0
            distinct_vals = set()
            j = i
            
            while j < n:
                mn = min(mn, p[j])
                mx = max(mx, p[j])
                g = math.gcd(g, p[j])
                distinct_vals.add(p[j])
                
                # If we have more than 2 distinct values, break
                if len(distinct_vals) > 2:
                    break
                
                # Check condition
                if mx - mn == g:
                    count += 1
                
                j += 1
            
            # Move to next start
            i += 1
        
        results.append(count)
    
    print("\n".join(map(str, results)))

if __name__ == "__main__":
    solve()