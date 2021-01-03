def nowrapsum(numbers):
    n = len(numbers)
    max = 0
    curr = 0
    for i in range(1, n):
        curr += numbers[i]
        if(curr < 0):
            curr = 0
        if(curr > max):
            max = curr
    return max

def main():
    try:
        filein = open("circlesum.in", "r")
        file = open("circlesum.out", "w")
        print("files opened")
        numbers = filein.readlines()
        numbers = [int(i) for i in numbers]
        #numbers = [28, 5, 10, 15, -2, -6, 45, -2, 10, 5, 2, 1, 20, 15, 14, 30, -2, 1, 35, 63, 2, 4 ,-7, 1, 6, 8, 12, 45, -6]
        n = len(numbers)
        nowrapmax = nowrapsum(numbers)
        print("function called")
        max = 0
        for i in range(1, n):
            max += numbers[i]
            numbers[i] = -numbers[i]
        max = max + nowrapsum(numbers)
        if max > nowrapmax:
            file.write(str(max))
        else:
            file.write(str(nowrapmax))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
