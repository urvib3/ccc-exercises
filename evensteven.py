def main():
    try:
        filein = open("evensteven.in", "r")
        file = open("evensteven.out", "w")
        sums = filein.readlines()
        sums = [int(i) for i in sums]
        for i in range(2,sums[0] + 1,2):
            print(i)
            file.write(str(i))
            file.write("\n")
        file.close()
    except:
        print("exception");
if __name__=="__main__":
    main()
