def main():
    try:
        filein = open("order.in", "r")
        file = open("order.out", "w")
        print("files opened")
        n = int(filein.readline())
        nums = filein.readline().split(' ')
        nums = [int(i) for i in nums]
        #nums = [0, 0, 0, 0, 1, 4, 4, 4, 4, 0]
        top = n
        for i in range(0,n):
            if(nums[i] == top):
                file.write(str(top))
                file.write("\n")
            top -= 1
        #file.write("test")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
