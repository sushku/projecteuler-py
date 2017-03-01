sum = 0
prev = 1
curr = 1
while curr < 4000000:
    if curr % 2 == 0:
        sum += curr
    prev, curr = curr, curr + prev
print(sum)
