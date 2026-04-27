import random




def max_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
            print("Minimum:", minimum)
    return minimum

def getValues():
    list = random.sample(range(1,100),6)
    # list = [5,4,3,2,1]
    print("List:", list)
    list_a = list[5]
    print("List A:",list_a)
    
list = random.sample(range(10), 6)
print(list)
print(list[2:])#Start at index 2
print(f"Stop at 3 {list[:3]}")#Stop at index 3
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list_a = list[-1] #get last index
print(list_a)
    
getValues()    
    
       