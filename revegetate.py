def main():
    try:
        filein = open("revegetate.in", "r")
        file = open("revegetate.out", "w")
        #print("files opened")
        
        # initialize n and m
        nums = filein.readline().split(' ')
        n,m = int(nums[0]), int(nums[1])
        
        # intialize 2 arrays to store preferences of cows
        a,b = [0]*m, [0]*m
        
        # array with types of all pastures
        t = [0]*(n+1)
        
        #print("arrays fine")
        
        #print("n: ", n, "m: ", m)
        
        # fill a and b
        for i in range(0,m):
            pair = filein.readline().split(' ')
            a[i] = int(pair[0])
            b[i] = int(pair[1])
            
            #print("in for loop")
            # if first pasture is larger, switch 2 pastures
            if a[i] > b[i]:
                c = a[i]
                a[i] = b[i]
                b[i] = c
            #print("swapped")
            #print("a: ", a, " b: ", b, " i: ", i)
                
        # loop through all n pastures
        for i in range(1,n+1):
            seed = 1
            
            #print("in second for loop")
            # loop through all types
            for type in range(1,5):
                free = True
                #print("in type for loop")
                
                # loop through all cow preferences
                    # if current pasture is adjacent to other pasture already processed,
                       # check if current type is still available
                for p in range(0,m):
                    #print("in ", p, " for loop")
                    if(b[p] == i and t[a[p]] == type):
                        free = False
                        break
                if(free):
                    seed = type
                    break
            t[i] = seed
            file.write(str(seed))
        #file.write("test")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
