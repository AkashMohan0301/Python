# num1 = float(input("Enter First Number :"))
# num2 = float(input("Enter Second Number :"))
# num3 = num1 + num2
# print(num3)   without function

num1 = float(input("Enter First Number :")) #with funtion 
num2 = float(input("Enter Second Number :"))

def add(num1,num2):
    c=num1+num2
    return c

print("sum=",add(num1,num2))

