def dimCheck():

    try:
        print("st1")
        print("st1")
        #return 10

    # '''(except only execute when try block have some error code)'''
    except TypeError :  #( must be child of next excepts)
        print("st1")
        print("st1")
        return 21

    except Exception :  #( must be parent of previous excepts)
        print("st1")
        print("st1")
        return 22

    # '''(else only execute when try block executed successfully)'''
    else:
        print("st1")
        print("st1")
        return  30

    # '''(anyway finally we definately execute even try execute successfully or not)'''
    finally:
        print("st1")
        print("st1")
        return  40
    return 50

'''
check return scenario with concepts by commenting the return statement
'''