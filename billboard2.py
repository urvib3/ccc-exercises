def covered(x,y,x3,y3,x4,y4):
    if(x>=x3 and x<=x4 and y>=y3 and y<=y4):
        return true
    else:
        return false
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
        print("matrix filled")
        redcorners = {{nums[0,0], nums[0,1]}, {nums[0,0], nums[0,3]}, {nums[0,2], nums[0,1]}, {nums[0,2], nums[0,3]}}
        bluecorners = {{nums[1,0], nums[1,1]}, {nums[1,0], nums[1,3]}, {nums[1,2], nums[1,1]}, {nums[1,2], nums[1,3]}}
        cornerscovered = 0
        print("arrays initialized")
        for i in range(0,3):
            if covered(redcorners[i][0], redcorners[i][1], nums[1,0], nums[1,1], nums[1,2], nums[1,3]):
                cornerscovered+=1
                print("cornerscovered: ", cornerscovered)
        if(cornerscovered < 2):
            print(nums[0,2]-nums[0,0])
            print(nums[0,3]-nums[0,1])
            answer = (nums[0,2]-nums[0,0])*(nums[0,3]-nums[0,1])
            print("less than 2 corners covered")
        elif(cornerscoverd == 4):
            answer=0
            print("all corners covered")
        else:
            leftx = max(nums[0,0], nums[1,0])
            rightx = min(nums[0,2], nums[1,2])
            lowy = max(nums[0,1], nums[1,1])
            highy = min(nums[0,3], nums[1,3])
            answer = (nums[0,2]-nums[0,0])*(nums[0,3]-nums[0,1]) -(rightx-leftx)*(highy-lowy)
            print("2 corners covered")
        file.write(str(int(answer)))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
