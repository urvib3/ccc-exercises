def main():
    try:
        filein = open("radio.in", "r")
        file = open("radio.out", "w")
        print("files opened")
        nums = filein.readlines()
        print(nums)
        nk = nums[0].split(' ')
        print("nk split")
        nk = [int(i) for i in nk]
        print("nk converted to int")
        print("nk, ", nk)
        for i in range(1, len(nums)):
            nums[i] = int(nums[i])
        print(nums)
        print("nums converted to int")
        #nk = filein.readline().split(' ')
        #nk = [int(i) for i nk]
        #nums = [0, 0, 0, 0, 1, 4, 4, 4, 4, 0]
        minn = nums[1]
        maxn = minn
        mink = nums[nk[0]+1]
        maxk = mink
        print("all variables initialized")
        for i in range(1, nk[0]):
            print("in n for loop")
            if(nums[i] < minn):
                print("in n min loop")
                minn = nums[i]
            elif(nums[i] > maxn):
                print("in n max loop")
                maxn = nums[i]
        for i in range(nk[0] + 1, len(nums)):
            print("in k for loop")
            if(nums[i] < mink):
                print("in k min loop")
                mink = nums[i]
            elif(nums[i] > maxk):
                print("in k max loop")
                maxk = nums[i]
        file.write(str(max(maxk-minn, maxn-mink)))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
