def main():
    try:
        filein = open("proximity.in", "r")
        file = open("proximity.out", "w")
        print("files opened")
        
        # read file and record n & k
        nk = filein.readline().split(' ')
        n, k = int(nk[0]), int(nk[1])
        '''n,k = 20, 4
        nums = [1,3,4,1,5,6,7,4,7,8,5,8,9,8,7,0,1,2,1,3]'''
        print("read file")
        
        # max breed id
        max = -1
           
        # array with breed ids of each cow; index = cow position in line
        cows = [0] * n
        
        # array with indices = breed id, value = within k elements(0/1)
        ids = [0] * 1000000
        #print("ids: ", ids)
        
        # loop through all n lines of cows
        for i in range(0,n):
            #print("in for loop")
            cows[i] = int(filein.readline().strip())
            #print("i: ", i, "i-k-1: ", i-k-1, " cows: ", cows)
            if(i-k-1 >= 0):
                print("removing ", i-k-1, " pos from recent k elements")
                ids[cows[i-k-1]] = 0
            #print("after first if loop")
            #print("first statement: ", ids[cows[i]] == 1)
            #print("second statement: ", cows[i] > max)
            if(ids[cows[i]] == 1 and cows[i] > max):
                #print("updating max")
                max = cows[i]
            ids[cows[i]] = 1
            #print("ids: ", ids)
       
        #file.write("test")
        file.write(str(max))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
