line = None

while line != 'done':
    line = input("Type done to complete: ")
    print("<", line, ">")

print("Loop complete")

# while loop repeats until the condition is false

myl = [23, 67, 32, 9, 77]
while myl:
    print(myl.pop() * 2)

# pop function takes the last number away and multiplies it by 2
