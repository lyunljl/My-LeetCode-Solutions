x = 12321
if x < 0 or (x != 0 and x % 10 == 0):
    print(False)
middle = 0
while x > middle:
    middle = (middle * 10) + (x % 10)
    x = x//10
print(x == middle or x == middle//10)