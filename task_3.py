from collections import Counter
jewels = input().strip()
stones = input().strip()
diff = Counter(stones) | Counter(jewels)
print(sum(diff.values()))
result = 0
for stone in stones:
    if stone in jewels:
        result += 1

print(result)
