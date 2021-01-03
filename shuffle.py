def main():
    try:
        filein = open("shuffle.in", "r")
        file = open("shuffle.out", "w")
        print("files opened")
        n = int(filein.readline())
        #n=10
        
        # array with shuffle from input
        shuffle = filein.readline().split(' ')
        shuffle = [int(i)-1 for i in shuffle]
        #shuffle = [0,1,0,3,2,4,9,8,2,6]
        print("shuffle: ", shuffle)
        
        # array with the number of times a cow is pointed to each position
        pointers = [0] * n
        print("pointers: ", pointers)
        
        # queue with all dead positions
        from queue import Queue
        q = Queue(maxsize = n)
        # number of positions processed through queue
        dead = 0
        print("queue: ", q, " dead: ", dead)
        print("queuesize: ", q.qsize())
        
        # loop through all numbers in array and fill pointers
        for i in range(0,n):
            pointers[shuffle[i]] += 1
        print("pointers: ", pointers)
        
        # add all positions with value 0 in pointers to queue
        for i in range(0,n):
            if(pointers[i] == 0):
                print("pos: ", i, " has a value of 0")
                q.put(i)
        print("filled queue: ", q)
        print("queuesize: ", q.qsize())
                
        # process queue until empty
        while(q.empty() == False):
            print("dead: ", dead, " current queue: ", q)
            dead += 1
            pos = q.get()
            dest = shuffle[pos]
            pointers[dest] -= 1
            if(pointers[dest] == 0):
                q.put(dest)
        print("final pointers: ", pointers)
        
        # output total number of locations - locations processed through queue
        #file.write("test")
        file.write(str(n-dead))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
