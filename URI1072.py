counter=int(input())
inRange=int(0)
outRange=int(0)
for i in range (1, counter+1):
    number = int(input())
    for j in range (10, 20+1):

        if(number==j):
            inRange=inRange+1

outRange=counter-inRange
print(str(inRange)+" in")
print(str(outRange)+" out")

