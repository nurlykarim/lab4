def divisible_generator(n):
    for i in range(0, n + 1, 12):
        yield i

n = int(input())

first = True
for num in divisible_generator(n):
    if not first:
        print(" ", end="")
    print(num, end="")
    first = False