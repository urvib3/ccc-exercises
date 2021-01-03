def main():
    try:
        filein = open("shell.in", "r")
        file = open("shell.out", "w")
        print("files opened")
        n = int(filein.readline())
        print("n read")
        guesses = [0,0,0]
        shells = [1,2,3]
        print("arrays initialized")
        for i in range(0,n):
            print("i in for loop: ", i)
            swaps = filein.readline().split(' ')
            print("line split: ", swaps)
            s1,s2,guesspos = int(swaps[0])-1, int(swaps[1])-1, int(swaps[2])-1
            print("s1: ", s1, " s2: ", s2, " guesspos: ", guesspos)
            # swap
            p = shells[s1] #p = 1
            shells[s1] = shells[s2]
            shells[s2] = p
            print("swap for i: ", i, " completed. shells: ", shells)
            #calculate guesses
            guess = shells[guesspos]
            print("shell guessed was: ", guess)
            guesses[guess-1] += 1
            print("current scores are: ", guesses)
        print("max guess is: ", max(guesses))
        file.write(str(max(guesses)))
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
