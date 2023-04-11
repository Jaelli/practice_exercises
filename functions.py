def demo_no_params():
    print("-"*20)
# if this function is called it will print 20 hyphens
# you do not need to use 'print' every time


# defining the function and creating variables included
def make_list(val, times):
    demo_no_params()
    result = str(val) * times
    return result
# functions can be called from within other functions


function_value = make_list("Test", 5)
print(function_value)
print(make_list("blah ", 3))


def change_list(inlist, val, times):
    inlist += str(val) * times


mylist = []
change_list(mylist, 'h', 8)
print(mylist)
