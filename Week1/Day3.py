import sys
def cal(A, exp, B):
	if exp == '+':
		return A + B
	elif exp == '-':
		return A - B
	elif exp == '*':
		return A * B
	else:
		return A//B
	
N = int(sys.stdin.readline())
answer = 0
for _ in range(N):
	A, exp, B = sys.stdin.readline().strip().split()
	answer += cal(int(A), exp, int(B))
print(answer)