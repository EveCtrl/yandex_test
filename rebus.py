n = int(input())
W = [0] + input().split()
W = [int(elem) for elem in W]

from string import ascii_lowercase
values = list((ascii_lowercase + ' '))
keys = [2**i for i in range(len(values))]
d = dict(zip(keys, values))

result = ''
for i in range(1, len(W)):
	dif = abs(W[i]- W[i-1])
	result += d[dif]
print(result)