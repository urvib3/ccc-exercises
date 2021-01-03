# https://developer.apple.com/ios/submit/
def main():
    try:
        filein = open("buckets.in", "r")
        file = open("buckets.out", "w")
        print("files opened")
        
        # create a queue with numbers 0-7 for each cow
        # create a processed list for all numbers that have gone through queue and been assigned position in a deque
        # have a pair that states the current cows that need to be placed next to current cow with x being less than y
        # if processed continue
        # if the current cow is x, append it to the left
        # elif the current cow is y, append it to the right
        # else append to left it's smaller than first number
            # else append it to right
        # continue until queue is empty
        # OR
        # first completely finish left side; while(this cow still needs a cow to its left)
        # then completely finish right side
        # finally, add the last cows based on whether they're smaller or larger than first number
        # instead of using matrix, just go through all pairs
        
        # go through cows from 0 to 7
        # have 2 lists of relations so that the first list of pairs is less than the second list
            # if the current cow is in the second list, it means that one of the cows that it should have been next to(the one in the first list) should already be in the list becuause it was of lower value
            # go through list and insert current cow right after the cow that came before it(cow in first list corresponding to the current cow)
            # if it does not have a conveninent pointer like above
                # initially have it's insertion be at last position
                # go through list until an element is larger than current element
                    # using the lists, check if it's possible for the current cow to be inserted right before that larger element
                    # if not, keep continuing until spot is found, change the position to that spot, and break out of the function
                    # insert the element at the correct position
        
        file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
