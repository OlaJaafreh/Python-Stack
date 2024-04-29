import random
def randInt(min= None  , max= None  ):
    if min== None and max== None:
        num = random.random()*100
    elif min!= None and max== None:
        num = random.random()*(100 - min)+min
    elif max!= None and min== None:
        num = random.random() * max
    else :
        num = random.random() * (max-min) + min
    return round(num)
print(randInt())# should print a random integer between 0 to 100
print(randInt(max=50))# should print a random integer between 0 to 50
print(randInt(min=50))# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500

