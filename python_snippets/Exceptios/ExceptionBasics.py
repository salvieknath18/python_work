"""password = "pass123"
count = 0
while True:
    try:
        user_value = input("Enter Password")
        assert user_value==password
    except AssertionError:
        count += 1
        if count == 3:
            print("Mar Ja")
            break
        print("Please Enter Valid Password")
    else:
        print("you are logged in")
        break
    finally:
        print("finally end")
"""
class TooOldError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

age = int(input("Enter Age"))

if age > 150:
    print("You are too old")
    raise TooOldError("You are too old")
