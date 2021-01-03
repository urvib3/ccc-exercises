def main():
    try:
        filein = open("cowsignal.in", "r")
        file = open("cowsignal.out", "w")
        print("files opened")
        nk = filein.readline().split(' ')
        n = int(nk[1])
        k = int(nk[2])
        sigs = filein.readlines()[0:]
        print(sigs)
        for sig in sigs:
            #print("inside for loop")
            ksig = ""
            for i in range(0,n):
                #print("inside 2nd for loop")
                c = sig[i]
                print(c)
                for _ in range(0,k):
                    #print("inside 3rd for loop")
                    ksig += c
            for _ in range(0,k):
                #print("inside 4th for loop")
                file.write(ksig)
                file.write("\n")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
