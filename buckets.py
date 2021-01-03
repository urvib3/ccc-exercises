# https://developer.apple.com/ios/submit/
def main():
    try:
        filein = open("buckets.in", "r")
        file = open("buckets.out", "w")
        print("files opened")
        
        # initialize coordinates for barn, lake, and rock
        bx, by, lx, ly, rx, ry = -1, -1, -1, -1, -1, -1
        numofr = 0
        
        # read file and assign coordinates
        rows = filein.readlines()
        for i in range(0,10):
            columns = list(rows[i])
            print("columns, ", columns)
            b = columns.count('B')
            l = columns.count('L')
            r = columns.count('R')
            print("counts for i: ", i, " ", b,l,r)
            if(b == 1):
                bx = columns.index('B')
                by = i
            if(l == 1):
                lx = columns.index('L')
                ly = i
            if(r >= 1):
                rx = columns.index('R')
                ry = i
                numofr+=columns.count('R')
        if(numofr > 1):
            columns.count('F')
        
        # absolute distance in x and y between barn and lake
        width = abs(bx-lx)
        length = abs(by-ly)
        print("width: ", width, " length: ", length)
        
        # if length is 0, check if rock is between them
        if(length == 0):
            if(ry == by and rx > min(bx,lx) and rx < max(bx,lx)):
                file.write(str(width+1))
            else:
                file.write(str(width-1))
            return;
        
        # if width is 0, check if rock is between thme
        if(width == 0):
            if(rx == bx and ry > min(by, ly) and ry < max(by,ly)):
                file.write(str(length+1))
            else:
                file.write(str(length-1))
            return;
         
        # if both width and length is greater than 0, there are 2 optimal paths, so rock isn't a problem
            # return width+length - 1(corner)
        file.write(str(width+length-1))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
