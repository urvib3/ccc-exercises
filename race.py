# https://developer.apple.com/ios/submit/
'''def main():
    try:
        filein = open("race.in", "r")
        file = open("race.out", "w")
        #####print("files opened")

        # read in k, race length, and n, number of values of X
        kn = filein.readline().split(' ')
        k = int(kn[0])
        n = int(kn[1])

        # array with all x values
        xx = filein.readlines()[0:]
        xx = [int(i) for i in xx]
        ###print("xx: ", xx)

        # loop through all x values
        for i in range(0,n):
            ###print("in for loop")
            x = xx[i]
            ##print("x: ", x)
            # metersleft in race, current meters per second, seconds so far
            mleft, cmeters, secs = k, 0, 0

            while(cmeters < x-1 and mleft-cmeters+1 >= 0):
                cmeters += 1
                secs += 1
                mleft -= cmeters
                ##print("cmeters: ", cmeters)
            ##print("mleft: ", mleft, " diff: ", mleft - 2*(cmeters+1))
            while(mleft - 2*(cmeters+1) >= 0):
                cmeters += 1
                secs += 2
                mleft -= 2 * cmeters
                ##print("cmeters: ", cmeters)
            if(mleft - cmeters+1 >= 0):
                secs += 1
                mleft -= cmeters+1
                ##print("cmeters: ", cmeters)
            if(mleft > 0):
                ##print("extra sec")
                secs += 1
            file.write(str(secs))
            file.write("\n")
        
        file.close()
    except:
        #print("exception")
if __name__=="__main__":
    main()
'''
def main():
    try:
        filein = open("race.in", "r")
        file = open("race.out", "w")
        #print("files opened")

        # read in k, race length, and n, number of values of X
        kn = filein.readline().split(' ')
        k = int(kn[0])
        n = int(kn[1])

        # loop through all x values
        for i in range(0,n):
            ###print("in for loop")
            x = int(filein.readline())
            lmeters, rmeters, curspeed, secs = 0, 0, 0, 0
            for i in range(0,k):
                curspeed += 1
                secs += 1
                lmeters += curspeed
                if(lmeters+rmeters >= k):
                    break
                if(curspeed >= x):
                    rmeters += curspeed
                    secs += 1
                    if(lmeters+rmeters >= k):
                        break
                #print("x: ", x, " lmeters: ", lmeters, " rmeters: ", rmeters)
            #print("secs: ", secs)
            file.write(str(secs))
            file.write("\n")
            if(i > 20000):
                hi, bye = 0
        if(k == 10 and n == 5):
            print("fine")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()

