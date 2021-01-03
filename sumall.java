
import java.io.*;
import java.util.*;
public class sumall {
	public static void main(String[] args){
		try {
			System.out.println("hi");
			FileReader fr = new FileReader("sumall.in");
			BufferedReader br = new BufferedReader(fr);
			FileWriter out = new FileWriter("sumall.out");
			int n = Integer.parseInt(br.readLine());
			int sum = 0;	
				for(int x=0; x < n; x++) {
					int i = Integer.parseInt(br.readLine());
					sum += i;
				}
			out.write(String.valueOf(sum));
			out.close();
     		}
		catch(Exception e) {
			System.out.println("exception");
		}
	}
}

