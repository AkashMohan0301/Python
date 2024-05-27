def day_year(d):
    years = d//365
    weeks = (d%365) // 7
    days = (d%365) % 7
    return years,weeks,days

try:

    days=float(input("Enter no of days :??"))
    x=isinstance(days,float)
    if days < 0:
        raise ValueError("Enter valid no of days")
    x,y,z=day_year(int(days))
    print("Years : ",x)
    print("Weeks : ",y)
    print("Days : ",z)

except ValueError as e:
    print(e)