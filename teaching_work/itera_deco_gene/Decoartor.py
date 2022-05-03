def decor(func):
    def infunc(name):
        if name == "ABCD":
            print("Bad Luck")
        else:
            func(name)
    return infunc


@decor
def wish1(name):
    print("Hello {}, Good Luck".format(name))


wish1("abhishek")
wish1("ABCD")


def wish2(name):
    print("Again Hello {}".format(name))


decorfunc = decor(wish2)
wish2("abhishek")
decorfunc("abhishek")
wish2("ABCD")
decorfunc("ABCD")


def decfunc1(func):
    print("inside decfunc1")

    def inner():
        x = func()
        print(x*x)
        return x*x
    return inner


def decfunc2(func):
    print("inside decfunc2")

    def inner():
        x = func()
        print(2*x)
        return 1000
    return inner


@decfunc1
@decfunc2
def num():
    return 10


print(num())
