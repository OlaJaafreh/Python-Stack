def BiggieSize(list):
    for i in range (len(list)):
        if list[i]>0:
            list[i]="big"
    return list
print(BiggieSize([-1, 3, 5, -5]))
print(BiggieSize([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")

def CountPositives(list):
    count=0
    for i in range (len(list)):
        if list[i]>0:
            count+=1
    list[len(list)-1]=count
    return list
print(CountPositives([-1,1,1,1]))
print(CountPositives([1,6,-4,-2,-7,-2]))

print("*************************************")


def SumTotal(list):
    sumList=0
    for i in range (0,len(list)):
        sumList=list[i]+sumList
    return sumList
print(SumTotal([-1, 3, 5, -5]))
print(SumTotal([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")

def Average(list):
    count=0
    sumList=0
    for i in range (0,len(list)):
        sumList=list[i]+sumList
        count+=1
    return sumList/count
print(Average([1, 2, 3, 4]))
print(Average([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")


def Length(list):
    count=0
    for _ in list:
        count+=1
    return count
print(Length([1, 2, 3, 4]))
print(Length([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")


def Minimum(list):
    min = list[0]
    for i in range (0,len(list)):
        if list[i]<=min:
            min =list[i]
        else: pass
    return min
print(Minimum([-1, 3, 5, -5]))
print(Minimum([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")


def Maximum(list):
    max = list[0]
    for i in range (0,len(list)):
        if list[i]>=max:
            max =list[i]
        else: pass
    return max
print(Maximum([-1, 3, 5, -5]))
print(Maximum([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")

def ultimate_analysis(list):
    new_person = {'sumTotal': SumTotal(list), 'average': Average(list), 'minimum': Minimum(list), 'maximum': Maximum(list), 'Length': Length(list)}
    return (new_person)
print(ultimate_analysis([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")

def reverse_list(list):
    flag1=0
    flag2=len(list)-1
    while flag1<flag2:
            temp=list[flag1]
            list[flag1]=list[flag2]
            list[flag2]=temp
            flag1+=1
            flag2-=1
    return list
print(reverse_list([-1, 3, 5, -5]))
print(reverse_list([-1, 11, 3, 5, -5 ,-2]))

print("*************************************")

