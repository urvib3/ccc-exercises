def winner(p1, p2):
    if(p1 == 1 and p2 == 2):
        return True
    elif(p1 == 2 and p2 == 3):
        return True
    elif(p1 == 3 and p2 == 1):
        return True
def main():
    try:
        filein = open("hps.in", "r")
        file = open("hps.out", "w")
        print("files opened")
        n = int(filein.readline())
        
        # initialize array for plays of each cow
        cow1, cow2 = [0]*n, [0]*n
        print("cow1 & 2 initialized: ", cow1, cow2)
        
        # all possible combinations
            # 1. 1 > 2 > 3 > 1
                # a. hoof, scissors, paper
                # b. paper, hoof, scissors
                # c. scisors, paper, hoof
            # 2. 1 < 2 < 3 < 1
                # a. paper, scissors, hoof
                # b. scissors, hoof, paper
                # c. hoof, paper, scissors
        
        # read file and fill cow1 & cow2
        for i in range(0,n):
            set = filein.readline().split(' ')
            cow1[i] = int(set[0])
            cow2[i] = int(set[1])
        print("files read and cow1 & cow2 filled: ", cow1, cow2)
            
        # max times cow1 wins with combinations 1 & 2
        score1, ties = 0, 0
        
        # cycle through all sets and calculate scores in each case
        for i in range(0,n):
            play1 = cow1[i]
            play2 = cow2[i]
            if(play1 == play2):
                ties += 1
            elif(winner(play1, play2)):
                score1 += 1
        #if(score1 + (n-ties-score1) + ties != n):
            #return;
        # output the max score of either combination
        file.write(str(max(score1, n-ties-score1)))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
