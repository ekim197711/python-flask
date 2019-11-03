try:
    myfile = open('myfile.txt')
    content = myfile.read()
    print(f'This is the content of the file {content}')
    number1 = int(input('Give me a number to divide 10 with'))
    result = 10 / number1
    print(f'Result: {result}')
except FileNotFoundError as err:
    print(f'We had an error opening the file: {err}')
except TypeError as err:
    print(f'We had an error dividing numbers: {err}')
except ZeroDivisionError as err:
    print(f'We cant divide with zero: {err}')
else:
    print(f'No exception occured... YES Lets continue the program')
finally:
    print(f'Do some cleanup the file operation is done')

