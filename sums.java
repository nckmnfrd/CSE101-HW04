//Nicholas Manfredi
//110207186
//CSE 101
//Lab Section 8
//Homework 4 

import java.util.Scanner;

public class sums {
	public static void main(String[] args){
		Scanner reader = new Scanner (System.in);
		System.out.print("Enter a Positive Integer: ");
		int n = reader.nextInt();
		while (n > 0) 
		{
			String s = Integer.toString(n);
			int sum = 0;
			for (int i = 1; i <= s.length(); i ++){
				int v =Integer.parseInt( s.substring(i - 1, i));
				sum += v*i;
			}
			System.out.println("Weighted Sum of Digits: " + Integer.toString(sum));
			System.out.print("Enter a Postive Integer: ");
			n = reader.nextInt();
		}
	}
}
