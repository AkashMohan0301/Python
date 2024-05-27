# Python program to check
# if a string is palindrome
# or not
def palidrom_simple(a):
    x = a
    w = ""
    for i in x:
        w = i + w
    if x == w:
        return "Yes"
    else:
        return "No"
y=input("Enter the String:")
print(palidrom_simple(y))
