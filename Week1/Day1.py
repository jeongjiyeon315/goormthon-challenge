import sys
W, R = map(int, sys.stdin.readline().split())
answer = W*(1 + (R/30))
print(int(answer))