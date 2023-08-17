import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

idx = arr.index(max(arr))
arr1 = arr[:idx+1]
arr2 = sorted(arr1)

if arr1 == arr2:
	arr1 = arr[idx+1:]
	arr2 = sorted(arr1, reverse=True)
	if arr1 == arr2:
		print(sum(arr))
	else:
		print(0)
else:
	print(0)