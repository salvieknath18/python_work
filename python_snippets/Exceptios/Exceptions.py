import sys

try:
    number = input('Enter a number: ')
    if number < 0:
        raise ValueError('Number is negative, Please Enter positive number')  # User Created Exception
    print('Division of 100 by number {} is {}'.format(number, 100/number))
except ZeroDivisionError:
    print("Plase enter number other than 0")
    try:
        number = int(input('Enter a number: '))
        print('Division of 100 by number {} is {}'.format(number, 100 / number))
    except ZeroDivisionError:
        print("Again the same mistake")
    except Exception:
        print("This is the error msg")
        print(sys.exc_info()[0])
except NameError as N:
    print("Got an Error : ", N)  # object of NameError Class
    print(sys.exc_info()[0])  # to get the Error name for the Exception
except Exception as E:    # for generic Exceptions
    print('Error: ', E) # gives the error message
    print(sys.exc_info()[0])  # to get the Error name for the Exception
else:  # Else executed only when the try block execute successfully without Exception
    print('Else Executed')
finally: # Finally execute Every time when the program enters in try and then with or without exception even we have exit inside try
    print('finally executed')
print("Program is completed")