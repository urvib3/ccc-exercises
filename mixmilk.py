def main():
    try:
        filein = open("mixmilk.in", "r")
        file = open("mixmilk.out", "w")
        print("files opened")
        bucket1 = filein.readline().split(' ')
        c1, m1 = int(bucket1[0]), int(bucket1[1])
        bucket2 = filein.readline().split(' ')
        c2, m2 = int(bucket2[0]), int(bucket2[1])
        bucket3 = filein.readline().split(' ')
        c3, m3 = int(bucket3[0]), int(bucket3[1])
        print("all buckets read")
        for i in range(0,100):
            print("in ", i, " for loop and remainder is: ", i%3)
            # bucket 1 to 2
            if(i%3 == 0):
                print("in if loop for bucket 1 to 2")
                print("m1: ", m1)
                milkpoured = min(c2-m2,m1)
                print("m1: ", m1, " m2: ", m2, " milkpoured: ", milkpoured)
                m2+=milkpoured
                m1-=milkpoured
            # buctet 2 to 3
            elif(i%3 == 1):
                milkpoured = min(c3-m3,m2)
                m3+=milkpoured
                m2-=milkpoured
            # bucket 3 to 1
            else:
                milkpoured = min(c1-m1,m3)
                m1+=milkpoured
                m3-=milkpoured
        file.write(str(m1))
        file.write("\n")
        file.write(str(m2))
        file.write("\n")
        file.write(str(m3))
        file.write("\n")
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
