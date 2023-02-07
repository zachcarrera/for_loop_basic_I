# 1. Basic
for i in range(151):
    print(i)

# 2. Multiples of Five
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)

# 3. Counting, the Dojo Way
for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


# 4. Whoa. That Sucker's Huge
sum_to_half_million = 0
for i in range(0, 500000):
    if i % 2 == 1:
        sum_to_half_million += i
print(sum_to_half_million)

# 5. Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# 6. Flexible Counter
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)
