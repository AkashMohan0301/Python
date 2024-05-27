def max_and_min(a):
    lists=a
    mx=0
    for i in lists:
        if i > mx :
            mx = i
    print(mx)

    
a=[]
n=int(input('Enter How many elements ?'))
for i in range(n):
    a.append(int(input('Enter the elements : ')))
max_and_min(a)