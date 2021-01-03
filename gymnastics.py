def main():
    try:
        import numpy as np
        filein = open("traffic.in", "r")
        file = open("traffic.out", "w")
        print("files opened")
        n = filein.readline()
        type = ["none"] * n
        mins = [0] * n
        maxes = [0] * n
        for i in range(0, n):
            parts = filein.readline().split(' ')
            type[i] = parts[0]
            mins[i] = parts[1]
            maxes[i] = parts[2]
        # calculate cars after mile n
        bmin, bmax = 0, 1000
        for i in range(0,n):
            if(type[i] == "on"):
                bmin += mins[i]
                bmax += maxes[i]
            elif(type[i] == "off"):
                bmin -= maxes[i]
                bmax -= mins[i]
            else(type[i] == "none"):
                bmin = max(bmin, mins[i])
                bmax = min(bmax, maxes[i])
        # calculate cars before mile 1
        tmin, tmax = 0, 1000
        for i in range(n,0,-1):
            if(type[i] == "on"):
                tmin -= maxes[i]
                tmax -= mins[i]
            if(type[i] == "off"):
                tmin += mins[i]
                tmax += maxes[i]
            if(type[i] == "none"):
                tmin = max(tmin, mins[i])
                tmax = min(tmax, maxes[i])
        file.write(str(tmin), " ", str(tmax))
        file.write("\n")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
