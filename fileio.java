
import java.io.*;
import java.util.*;
public class fileio{
	public static void main(String[] args){
		try {
		FileReader fr = new FileReader("fileio.in");
		BufferedReader br = new BufferedReader(fr);
		String s = br.readLine();
		FileWriter out = new FileWriter("fileio.out");
		out.write(s);
		out.close();
		}
		catch (Exception e) {
			System.out.println("exception");
		}

	}
}

