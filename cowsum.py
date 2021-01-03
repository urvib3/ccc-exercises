class Cow:
    def __init__(self, weight=0, height=0, width=0, length=0, ti=0, tj=0):
        self.weight = weight
        self.height = height
        self.width = width
        self.length = length
        self.ti = ti
        self.tj = tj
def main():
    try:
        filein = open("cowsum.in", "r")
        file = open("cowsum.out", "w")
        print("files opened")
        parts = filein.readline().split(' ')
        n = int(parts[0])
        t = int(parts[1])
        print("n&t initialized")
        cows = [Cow()]*n
        print("cow array initialized")
        for i in range(0,n):
            p = filein.readline().split(' ')
            p = [int(i) for i in p]
            cows[i] = Cow(p[0], p[1], p[2], p[3], p[4], p[5])
        print("cow array filled")
        wemax = -1
        hmax = -1
        wmax = -1
        lmax = -1
        for cow in cows:
            if(cow.ti <= t and cow.tj > t):
                if (cow.weight > wemax):
                    wemax = cow.weight
                if (cow.length > lmax):
                    lmax = cow.length
                if (cow.width > wmax):
                    wmax = cow.width
                if (cow.height > hmax):
                    hmax = cow.height
        print("maxes determined")
        file.write(str(wemax) + '\n' + str(hmax) + '\n' + str(wmax) + '\n' + str(lmax))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()

