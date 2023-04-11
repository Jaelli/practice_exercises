import sys

for arg in sys.argv:
    print("Cmd line argument: ", arg)

print()

for idx, arg in enumerate(sys.argv):
    print('index:', idx, 'argument:', arg)

print()
