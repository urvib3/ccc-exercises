import java.util.*;
import java.io.*;
public class circlesum {
public static void main(String[] args){
    try{
	FileReader fr = new FileReader("circlesum.in");
	BufferedReader br = new BufferedReader(fr);
        FileWriter out = new FileWriter("circlesum.out");
        System.out.println("files opened");
	int seeds = Integer.parseInt(br.readLine());
	System.out.println("first number parsed");
	int[] numbers = new int[seeds];
	System.out.println("array made");
	numbers[0] = seeds;
	for(int x=1; x < seeds + 1; x++) 
		numbers[x] = Integer.parseInt(br.readLine());
	System.out.println("array finished");
        System.out.println("files converted");
        int begcirclength = 0;
        int index = 1;
        // finds sum of beginning positive numbers, added on to end of array sum
        System.out.println(numbers);
        while(index < numbers.length){
            if(numbers[index] < 0)
                break;
            begcirclength += numbers[index];
            index ++;
	}
        System.out.println("begcirclength: " + begcirclength);
        int max = begcirclength;
        int cursum = 0;
        for (int i=index; i < seeds; i++) {
            if(numbers[i] > 0)
                cursum += numbers[i];
            else{
                if(cursum > max)
                    max = cursum;
                cursum = 0;
	    }
            System.out.println("cursum: " + cursum+ " after number: "+ numbers[i]);
	}
        if(cursum > 0){
            cursum += begcirclength;
            if(cursum > max)
                max = cursum;
	}
        String s = String.valueOf(max);
        out.write(s);
        out.close();
	}
    catch(Exception e) {
        System.out.println("exception");
    }
}
}
