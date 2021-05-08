n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

count1 = m // (k + 1)
count2 = m % (k + 1)

result = count1 * (first * k + second) + count2 * second

print(result)