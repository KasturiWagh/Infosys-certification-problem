arr = []                     #All sequences  
curr = []                    #Current value

def check(a):
    curr = a
    if (curr % 2 == 0):
        curr = a / 2
        arr.append(curr)
    elif (curr % 2 != 0):
        curr = ( a * 3) + 1
        arr.append(curr)
    elif (curr == 0):
        arr.append(0)

    while (arr[-1] != 1):
        check(curr)

val = []                      #Input values 
val = input().split()

last = []                     #Sequence count

for i in val :
    aval = int(i)
    if aval == 1:                      
        last.append(1)
    else:
        arr = []
        arr.append(aval)
        curr = aval
        check(curr)
        last.append(len(arr))

print(*last,sep = ",")
