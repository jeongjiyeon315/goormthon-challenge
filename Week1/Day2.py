import sys

N = int(sys.stdin.readline())
T, M = map(int, sys.stdin.readline().split())
time = T*60 + M
for _ in range(N):
	time += int(sys.stdin.readline())

H = time//60
M = time%60

if H >= 24:
	H = H%24
print(H, M)