import sys
    
str = sys.stdin.readline().strip()
n = len(str)
answer = (n * (n + 1)) // 2
cnt = [0] * 26
    
for i in range(n):
    cnt[ord(str[i]) - ord('a')] += 1
    
for i in range(26):
    answer -= (cnt[i] * (cnt[i] - 1)) // 2 + cnt[i]
print(answer + 1)
