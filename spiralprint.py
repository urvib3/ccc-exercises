def main():
    try:
        import math
        import numpy as np
        filein = open("spiralprint.in", "r")
        file = open("spiralprint.out", "w")
        print("files opened")
        n = int(filein.readline())
        print("n read")
        r = np.zeros((1,1))
        print("test matrix made")
        nums = np.zeros((n,n))
        print("matrix created")
        for i in range(0,n):
            parts = filein.readline().split(' ')
            for j in range(0, len(parts)):
                # might have to convert string to int
                nums[i,j] = parts[j]
        print("matrix filled")
        numofspirals = math.ceil(n/2)
        for a in range(0, numofspirals):
            print("for loop fine for a: ", a)
            for j in range(a, n-a):
                print("a: ", a, " n-a: ", n-a, "num: ", nums[a,j])
                file.write(str(int(nums[a, j])))
                file.write("\n")
            print("1st for loop fine for a: ", a)
            for i in range(a+1, n-a):
                file.write(str(int(nums[i, n-a-1])))
                file.write("\n")
            print("2nd for loop fine for a: ", a)
            for j in range(n-a-2, a-1, -1):
                file.write(str(int(nums[n-a-1, j])))
                file.write("\n")
            print("3rd for loop fine for a: ", a)
            for i in range(n-a-2, a, -1):
                file.write(str(int(nums[i, a])))
                file.write("\n")
            print("4th for loop fine for a: ", a)
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
