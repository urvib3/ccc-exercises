def onespace(x,y,z):
    if(x+2 == y):
        return True
    elif(x+2 == z):
        return True
    elif(y+2 == x):
        return True
    elif(y+2 == z):
        return True
    elif(z+2 == x):
        return True
    elif(z+2 == y):
        return True
        
def maxmoves(nums):
    nums.sort()
    firstgap = nums[1] - nums[0]
    secondgap = nums[2] - nums[1]
    return max(firstgap, secondgap)-1

def main():
    try:
        filein = open("herding.in", "r")
        file = open("herding.out", "w")
        print("files opened")
        
        # initialize nums with positions of cows
        nums = filein.readline().split(' ')
        nums = [int(i) for i in nums]
        print("nums: ", nums)
        
        # if all positions are consecutive, output min = 0, max = 0
        print("case 1: ", nums[0]+1 == nums[1] and nums[1]+1 == nums[2])
        print("case 2: ", nums[0]-1 == nums[1] and nums[1]-1 == nums[2])
        if((nums[0]+1 == nums[1] and nums[1]+1 == nums[2]) or (nums[0]-1 == nums[1] and nums[1]-1 == nums[2])):
            file.write("0\n0")
            return
        print("first if loop good")
        
        # elif 2 positions only have one space
        set = onespace(nums[0], nums[1], nums[2])
        if(set):
            file.write("1\n")
            # if the other gap is also 1 space, max = 1
            print("second if loop good")
        else:
            file.write("2\n")
        file.write(str(maxmoves(nums)))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
