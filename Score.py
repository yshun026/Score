scores = input().split()

count = 0
maxn = int(scores[0])
minn = int(scores[0])

for s in scores:
    if int(s) < 60:
        count += 1
    if int(s) > maxn:
        maxn = int(s)
    if int(s) < minn:
        minn = int(s)

print(count)
print(f"max: {maxn}, minn: {minn}")
