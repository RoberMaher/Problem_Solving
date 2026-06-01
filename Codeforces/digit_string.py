# B. Digit String
# time limit per test2 seconds
# memory limit per test512 megabytes
# You are given a string s
#  consisting of digits from 1
#  to 4
# .

# Let's say that the string is beautiful if it is impossible to select some of its elements and write them out (in the same order as they appear in the string) to form a number that is a multiple of 4
# . For example, the strings 31, 222, 213 are beautiful, while the strings 143, 3123, 1322 are not. The empty string is considered beautiful.

# Your task is to calculate the minimum possible number of elements in the string s
#  that need to be removed in order to make it beautiful.

# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.

# The only line of each test case contains a string s
#  (1≤|s|≤3⋅105
# ), consisting of digits from 1
#  to 4
# .

# Additional constraint on the input: the sum of the lengths of s
#  over all test cases doesn't exceed 3⋅105
# .

# Output
# For each test case, print a single integer — the minimum possible number of elements in the string s
#  that need to be removed in order to make it beautiful.

# Example
# InputCopy
# 5
# 4
# 13
# 3244123
# 24424224242
# 4132423432241231
# OutputCopy
# 1
# 0
# 4
# 5
# 9
# Note
# In the first example, you have to delete the whole string.

# In the second example, the string is already beautiful.

# In the third example, you can delete the 1
# -st, 3
# -rd, 4
# -th, and 6
# -th characters, and you will get the string 213.

t = int(input())
a = []

for _ in range(t):
    s = input().strip()
    
    dp = [0] * 5

    for ch in s:
        c = int(ch)

        new_dp = dp[:]

        if c != 4:
            new_dp[c] = max(new_dp[c], 1)

        for d in range(1, 5):
            if dp[d] == 0:
                continue
            if (d == 1 and c == 2):
                continue
            if (d == 2 and c == 4):
                continue
            if (d == 3 and c == 2):
                continue
            if (d == 4 and c == 4):
                continue
            if c == 4:
                continue

            new_dp[c] = max(new_dp[c], dp[d] + 1)

        dp = new_dp
    best = max(dp)
    a.append(str(len(s) - best))

print("\n".join(a))