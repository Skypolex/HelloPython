from random import randint

if __name__ == '__main__':
    print("Hello World")
    print("shift + enter 加一行")
    
    print("ok?")
    randomNumber1 = randint(0, 10)
    randomNumber2 = randint(0, 10)
    if randomNumber1 > randomNumber2:
        print("randomNumber1 is big")
    elif randomNumber1 == randomNumber2:
        print("randomNumber1 is equal")
    elif randomNumber1 < randomNumber2:
        print("randomNumber2 is big")
