def main():
    try:
      import math
      import numpy as np
      filein = open("billboard.in", "r")
      file = open("billboard.out", "w")
      print("files opened")
      nums = np.zeros((2,4))
      print("matrix created")
      for i in range(0,2):
          parts = filein.readline().split(' ')
          for j in range(0, len(parts)):
              nums[i,j] = int(parts[j])
      x1, y1 = nums[0,0], nums[0,1]
      x2, y2 = nums[0,2], nums[0,3]
      x3, y3 = nums[1,0], nums[1,1]
      x4, y4 = nums[1,2], nums[1,3]
      width = x2-x1
      length = y2-y1
      xmin = max(x1,x3)
      xmax = min(x2,x4)
      ymin = max(y1,y3)
      ymax = min(y2,y4)
      cowbbwidth = nums[1,2]-nums[1,0]
      cowbblength = nums[1,3]-nums[1,1]
      print("common area dimensions: ", xmin, xmax, ymin, ymax)
      cwidth = xmax-xmin
      clength = ymax-ymin
      if(cwidth >= cowbbwidth+width or clength >= cowbblength+length):
          file.write(str(int(length*width)))
          return;
      elif(x1 < x3 and x4 < x1):
          file.write(str(int(length*width)))
          return;
      elif(y1 < y3 and y4 < y2):
          file.write(str(int(length*width)))
          return;
      elif(clength >= length):
          print("in if loop")
          width -= cwidth
      elif(cwidth >= width):
          length -= clength
      file.write(str(int(length*width)))
      print(x1,y1,x2,y2,x3,y3,x4,y4)
      print(nums)
      file.close()
    except:
        print("exception")
if __name__=="__main__":
    main()
