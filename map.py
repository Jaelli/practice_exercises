numbers = [1, 2, 3]

print(numbers)

def double(a):
    return a * 2

result = map(double, numbers)

print(list(result))
