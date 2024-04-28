for x in range(151):
    print(x)
print("######################################")


for x in range(5,1000,+5):
    print(x)
print("######################################")

for x in range(1,101,1):
    if x%10==0:
        y="Coding Dojo"
        print(y)
    elif x%5==0:
        y="Coding"
        print(y)
    else:
        print(x)
print("######################################")
y=0;
for x in range(500000):
    if x%2!=0:
        y=y+x
    else:
        pass

print(y)

print("######################################")

lowNum=2
highNum=9
mult=3

for x in range(lowNum,highNum+1):
    if x%mult==0:
        print(x)
    else:
        pass


