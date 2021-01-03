def main():
    try:
        import math
        import numpy as np
        filein = open("billboard.in", "r")
        file = open("billboard.out", "w")
        print("files opened")
        nums = np.zeros((2,4))
        print("matrix created")
        for i in range(0,2):
            parts = filein.readline().split(' ')
            for j in range(0, len(parts)):
                nums[i,j] = int(parts[j])
        '''
        file.write("testing")
        nums[0,0] = 1
        nums[0,1] = 0
        nums[0,2] = 4
        nums[0,3] = 5
        nums[1,0] = 0
        nums[1,1] = 3
        nums[1,2] = 6
        nums[1,3] = 8
        '''
        print("matrix filled")
        lheight = nums[0,3] - nums[0, 1]
        lwidth = nums[0, 2] - nums[0, 0]
        cheight = nums[1, 3] - nums[1,1]
        cwidth = nums[1,2] - nums[1,0]
        theight = lheight
        twidth = lwidth
        print("variables initialize")
        # l left/right = nums[0,0/2]; l bottom/top = nums[0, 1/3]
        # c left/right = nums[1,0/2]; c bottom/top = nums[1, 1/3]
        # cow billboard overlaps left or right side of lawn billboard
            # cow billboard is taller than lawn billboard
            # cow top is higher than lawn top
            # cow bottom is lower than lawn bottom
        if(cheight >= lheight and nums[1,3] >= nums[0,3] and nums[1,1] <= nums[0,1]):
            print("height conditional success")
            # if cowboard is to the left of lawn billboard & overlaps board
            if(nums[1,0] <= nums[0,0] and nums[1,2] > nums[0,0]):
                # tarp width - (cow right x - lawn left x)
                twidth -= nums[1,2] - nums[0,0]
            # if cowboard is to the right of lawn billboard & overlaps
            elif(nums[1,2] >= nums[0,2] and nums[1,0] < nums[0,2]):
                # tarp width - (lawn right - cow left)
                twidth -= nums[0,2] - nums[1,0]
        # if all width covered by cow billboard, return 0
        if(twidth <= 0):
            file.write("0")
            return
        # cow billboard overlaps top or right side of lawn billboard
            # cow billboard is wider than law billboard
            # cow left is lefter than lawn left
            # cow right is righter than lawn right
        if(cwidth >= lwidth and nums[1,0] <= nums[0,0] and nums[1,2] >= nums[0,2]):
            print("width conditional success")
            # if cowboard is higher than lawn billboard & overlaps
            if(nums[1,3] >= nums[0,3] and nums[1,1] <= nums[0,3]):
                print("higher overlap success")
                # tarp height - (lawn top - cow bottom)
                print("theight: ", theight, " diff: ", nums[0,3] - nums[1,1])
                theight -= nums[0,3] - nums[1,1]
            # if cowboard is lower than lawn billboard & overlaps
            elif(nums[1,1] <= nums[0,1] and nums[1,3] >= nums[0,1]):
                print("lower overlap success")
                # tarp height - (cow top - lawn bottom)
                theight -= nums[1,3] - nums[0,1]
        file.write(str(int(twidth*theight)))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
