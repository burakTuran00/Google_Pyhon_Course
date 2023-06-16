def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

values = [23,52,56,42,21]

sum = 0
length = 0

for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum)+ " and Average: " + str(sum/length))


def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print(x,to_celsius(x))



for left in range(7):
    for right in range(left, 7):
        print("["+str(left) + "|" + str(right)+ "]", end=" ")
    print()
