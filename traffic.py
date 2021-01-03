def main():
    try:
        filein = open("traffic.in", "r")
        file = open("traffic.out", "w")
        print("files opened")
        n = int(filein.readline())
        type = ["none"] * n
        mins = [0] * n
        maxes = [0] * n
        print("arrays initialized")
        for i in range(0, n):
            parts = filein.readline().split(' ')
            type[i] = parts[0]
            mins[i] = int(parts[1])
            maxes[i] = int(parts[2])
        '''
        n = 7
        type = ["on", "on", "none", "none", "off", "on", "none"]
        mins = [1,2,10,11,2,0,10]
        maxes = [1,4,14,15,3,1,11]
        '''
        print("arrays filled")
        # calculate cars after mile n
        bmin, bmax = 0, 1000
        for i in range(0,n):
            if(type[i] == "on"):
                bmin += mins[i]
                bmax += maxes[i]
            elif(type[i] == "off"):
                bmin -= maxes[i]
                bmax -= mins[i]
            else:
                bmin = max(bmin, mins[i])
                bmax = min(bmax, maxes[i])
        print("mile n range calculated")
        # calculate cars before mile 1
        tmin, tmax = 0, 1000
        for i in range(n-1,-1,-1):
            if(type[i] == "on"):
                tmin -= maxes[i]
                tmax -= mins[i]
            elif(type[i] == "off"):
                tmin += mins[i]
                tmax += maxes[i]
            else:
                tmin = max(tmin, mins[i])
                tmax = min(tmax, maxes[i])
            print("i: ", i, " tmin: ", tmin, " tmax: ", tmax)
        if(tmin < 0):
            tmin = 0
        if(tmax < 0):
            tmax = 0
        if(bmin < 0):
            bmin = 0
        if(bmax < 0):
            bmax = 0
        print("mile 1 range calculated")
        file.write("%s %s %s\n" % (tmin, " ", tmax))
        print("first output line written")
        file.write("%s %s %s" % (bmin, " ", bmax))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
