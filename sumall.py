def main():
    try:
        filein = open("sumall.in", "r")
        sums = filein.readlines()
        sums = [int(i) for i in sums]
        sum = 0;
        for i in range(1,sums[0] + 1):
            sum += sums[i]
        print(sum)
        file = open("sumall.out", "w")
        print("file opened")
        file.write(str(sum))
        print("file wrote")
        file.close()
    except:
        print("exception");
if __name__=="__main__":
    main()
