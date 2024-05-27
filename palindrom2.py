

def palindrom2(c):
    if c==c[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
        
x=input("Enter the string ")
x2=x.lower()
palindrom2(x2)