def far_to_cel(a):
    c=(a-32)*5/9
    return c
v=far_to_cel(float(input("Enter the Fahrenheit :")))
formatted_value="{:.4f}".format(v)
print(formatted_value)