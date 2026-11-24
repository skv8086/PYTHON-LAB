nums = list(map(int, input("Enter integers separated by space: ").split()))

pnum = []

for num in nums:
    if num > 0:
        pnum.append(num)

print("Original list:", nums)
print("Positive numbers:", pnum)
