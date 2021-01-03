def main():
    try:
        filein = open("copymachine.in", "r")
        file = open("copymachine.out", "w")
        numbers = filein.readlines()
        numbers = [int(i) for i in numbers]
        for i in range(1, numbers[0] + 1):
            file.write(str(numbers[i]))
            file.write("\n")
        file.close()
    except:
        print("exception");
if __name__=="__main__":
    main()
