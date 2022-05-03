
cnt = 0

while cnt<3:
    try:
        a = int(input("Enter number"))
        print(100/a)
        break
    except Exception as E:
        print("You Have an error of zero division please enter valid number")
        if cnt == 2:
            print("You are stupid")
        cnt +=1
            