def main():
    try:
        filein = open("reverseprint.in", "r")
        file = open("reverseprint.out", "w")
        print("files opened")
        numbers = filein.readlines()
        numbers = [int(i) for i in numbers]
        print("files converted")
        for i in range(numbers[0], 0, -1):
            print(i)
            file.write(str(numbers[i]))
            file.write("\n")
        file.close()
    except:
        print("exception");
if __name__=="__main__":
    main()
