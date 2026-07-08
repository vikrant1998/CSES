import sys
data = sys.stdin.buffer.read().split()
n, x = int(data[0]), int(data[1])
nums = list(map(int, data[2:2 + n]))

m = {}
for i, a in enumerate(nums):
	if x - a in m:
		print(i + 1, m[x - a] + 1)
		break
	m[a] = i
else:
	print("IMPOSSIBLE")
