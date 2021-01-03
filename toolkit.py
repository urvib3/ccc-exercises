def main():
    try:
        filein = open("toolkit.in", "r")
        file = open("toolkit.out", "w")
        print("files opened")
        n = int(filein.readline())
        nums = filein.readline().split(', ')
        instances = [0]*3
        print("instances filled")
        for tool in nums:
            if(tool == "bolt"):
                instances[0] += 1
            elif(tool == "nail"):
                instances[1] += 1
            else:
                instances[2] += 1
        print("tools done")
        for i in range(0, n-1):
            if(i < instances[0]):
                file.write("bolt, ")
            elif(i < instances[1]):
                file.write("nail, ")
            else:
                file.write("screw, ")
        print("stuff written out")
        if(instances[2] > 0):
            file.write("screw")
        elif(instances[1] > 0):
            file.write("nail")
        else:
            file.write("bolt")
        file.write("\n")
        file.write(str(instances[0]))
        file.write("\n")
        file.write(str(instances[1]))
        file.write("\n")
        file.write(str(instances[2]))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
