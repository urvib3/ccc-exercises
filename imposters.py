def main():
    try:
        filein = open("imposters.in", "r")
        file = open("imposters.out", "w")
        print("files opened")
        n = int(filein.readline())
        if(n==0):
            file.write("0")
        nums = filein.readline().split(' ')
        nums = [int(i) for i in nums]
        #nums = [0, 0, 0, 0, 1, 4, 4, 4, 4, 0]
        #print("nums array created")
        instances = [0]*10
        # current number in subarray
        c = -1
        # max length of contiguous subarray
        max = 0
        # length of current subarry
        cmax = 0
        # number with max instances
        maxn = -1
        print("variables initialized")
        for i in range(0,n):
            print("test for, we good")
        for i in range(0,n):
            print("n: ", n, " for loop good for i: ", i)
            instances[nums[i]] += 1
            print("instance i: ", i, " added")
            if(nums[i] != c):
                print("if loop good")
                cmax = 0
            cmax += 1
            c = nums[i]
            if(cmax > max):
                print("if inside else good")
                max = cmax
                maxn = c
                print("full else finished")
        file.write(str(instances[maxn]))
        #ile.write("test")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
