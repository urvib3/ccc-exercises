def main():
    try:
        filein = open("whereami.in", "r")
        file = open("whereami.out", "w")
        print("files opened")
        n = int(filein.readline())
        s = filein.readline()
        #s = "AAAABBB"
        print(s.find("A", 3))
        print(s)
        min = 0
        cmin = 0
        l,r = 0,1
        # make sure to check that start is inclusive or exclusive in find method
        print("n: ", n)
        while(r-l < n):
            cmin = r-l
            while(r < n):
                #print("while loop")
                cstring = s[l:r]
                print("cstring: ", cstring, "min: ", min)
                if(s.find(cstring, l+1) != -1):
                    #print("if loop")
                    min+=1
                    r+=1
                    #print("end if loop")
                else:
                    l+=1
                    r+=1
                    print("else loop")
            if(min == cmin):
                print("min didn't change")
                break
            l = 0
            r = min
            print("l: ", l, " r: ", r)
        print("before writing to file")
        #file.write("test")
        file.write(str(min))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
