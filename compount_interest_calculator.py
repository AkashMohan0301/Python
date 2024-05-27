def compount_interest(p,r,t):
    Amount=p*((pow(1+r/100,t)))
    CI=Amount-p
    return CI

p1=int(input("Enter The Principal Amount :"))
r1=float(input("Enter The rate of Interest :"))
t1=int(input("Enter The Years :"))
print(compount_interest(p1,r1,t1))