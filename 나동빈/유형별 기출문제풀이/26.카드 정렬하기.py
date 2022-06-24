import heapq

n = int(input())
arr = []
result = 0

for _ in range(n):
    heapq.heappush(arr, int(input()))

while arr:
    val1 = heapq.heappop(arr)

    if arr:
        val2 = heapq.heappop(arr)
    else:
        break

    sumVal = val1 + val2
    result += sumVal
    heapq.heappush(arr, sumVal)

print(result)