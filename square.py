def main():
    try:
        import math
        import numpy as np
        filein = open("square.in", "r")
        file = open("square.out", "w")
        print("files opened")
        nums = np.zeros((2,4))
        print("matrix created")
        for i in range(0,2):
            parts = filein.readline().split(' ')
            for j in range(0, len(parts)):
                nums[i,j] = int(parts[j])
        print("matrix filled")
        xmin = min(nums[0,0], nums[1,0])
        xmax = max(nums[0,2], nums[1,2])
        ymin = min(nums[0,1], nums[1,1])
        ymax = max(nums[0,3], nums[1,3])
        print("max and mins worked")
        print(nums)
        l = xmax-xmin
        w = ymax-ymin
        file.write(str(int(max(l*l, w*w))))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
