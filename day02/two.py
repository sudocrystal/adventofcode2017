import fileinput

def evenly(x,y):
    if y != 0 and x // y == x / y:
        return x // y
    else:
        return -1

total = 0

for line in fileinput.input(files="nums.txt"):
    nums = [int(i) for i in line.split()]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if i != j and evenly(nums[i],nums[j]) != -1:
                total += evenly(nums[i],nums[j])
                break
            elif i != j and evenly(nums[j],nums[i]) != -1:
                total += evenly(nums[j],nums[i])
                break
    
print(total)
