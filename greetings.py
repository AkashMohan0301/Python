def greetings(a,name):
    if a > 18:
        print("Hello,"+name+" you are an adult")
    else:
        print("Hello,"+name+" you are a kid")


name = input("What is your Name ?:")
age = int(input("What is your age ?:"))

greetings(age,name)