##countdown

def countdown(n):
     list=[]
     for x in range (n ,-1 ,-1):
          list.append(x)
     print (list)

countdown(5)

# Print and Return
def PandR (list):
     print(list[0])
     return list[1]


PandR((3,4))


#First Plus Length 
def First_Plus_Length(list):
     print (list[0]+len(list)) 

First_Plus_Length((1,2,3,4,5,6))


#Values Greater than Second
def ValuesGreaterthanSecond(list):
     count =0
     new_list=[]
     if len(list)<2:
          return False 
     else:

          for x in range(len(list)):
               if list[x]>list[1]:
                    count+=1 
                    new_list.append(list[x])
     return count,new_list

print(ValuesGreaterthanSecond([5]))


# This Length, That Value
def ThisLength_ThatValue(length,value):
     new_list=[]
     for x in range(length):
          new_list.append(value)
     return new_list
print(ThisLength_ThatValue(3,5))
