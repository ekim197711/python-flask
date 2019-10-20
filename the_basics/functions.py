def salestax(price, salestax=0.25):
    result = price * salestax
    return result


tax = salestax(100)
print(tax)


def helloPeople(greeting, *people):
    print(greeting)
    for p in people:
        print(p)


helloPeople("Hello and welcome my friend",
            "mike", "jens", "Natazcha", "Susanne",
            'Kim',
            'Søren')


def hello_people(**mydict):
    '''
    This method prints out stuff from a dictionary
    :param mydict:
    :return:
    We return nothing in our case... None
    '''
    for k in mydict:
        print("key: {}, value {}".format(k, mydict[k]))


hello_people(Mike=41, Jens=48, Susanne=50, Karen=30, Søren=27.5, tractor='green')
print("The documentation for our function is: {}".format(hello_people.__doc__))


def greeting(num):
    if num > 10:
        print("The number is high")
    elif num > 5:
        print('The number is medium high')
    else:
        print('We cant classify the number')


greeting(0)
greeting(6)
greeting(20)


def addnumbers(num1):
    return lambda num2: num1 + num2


mylambda = addnumbers(100)
print(mylambda(200))
print(mylambda(500))
print(mylambda(2))


def loopfunction(mynumber):
    i = 0
    while True:
        i = i + mynumber
        if i > 1000:
            break
        elif i == 900:
            continue

        print(i)


loopfunction(20)
