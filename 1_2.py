
file = open("1Input.txt")

sum = 0
#Hold list values
Llist = []
RList = []
#Populate list values
for line in file:
    a, b = line.split()
    Llist.append(int(a))
    RList.append(int(b))
#Sort lists
Llist.sort()
RList.sort()
#Iterate across values
for i in range(len(Llist)):
    num = Llist[i]
    sum+=num*RList.count(num)

print(sum)