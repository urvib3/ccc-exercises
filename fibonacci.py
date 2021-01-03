def main():
    try:
        filein = open("fibonacci.in", "r")
        file = open("fibonacci.out", "w")
        n = int(filein.readline())
        pnum = 0
        snum = 1
        cnum = 1
        if(n == 1):
            file.write("1")
            return
        for i in range(1, n):
            print("good")
        for i in range(1, n):
            print("cnum: ", cnum, " pnum: ", pnum, " ssum: ", snum)
            cnum = pnum + snum
            pnum = snum
            snum = cnum
        print(cnum)
        file.write(str(cnum))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()

