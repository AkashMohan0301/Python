def max_and_min(a):
    lists=a
    for i in lists:
        print(i)
    print("maximum =",max(lists))
    print("minimum =",min(lists))
    
a=[]
n=int(input('Enter How many elements ?'))
for i in range(n):
    a.append(int(input('Enter the elements : ')))
max_and_min(a)