x = 'main      '


def func():

    x = 'func      '
    print(x, id(x))

    def inner_func():
        nonlocal x
        x = 'inner_func'
        print(x, id(x))

    inner_func()
    print(x, id(x))


print(x, id(x))
print(111)
func()
print(x, id(x))