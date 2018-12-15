/**
 * 
 */
package com.learning.java;

import java.util.Random;

/**
 * @author Mohan Prasath Chinnasamy
 *
 */
public class Java_Examples {

	/**
	 * @param args
	 * 
	 * This comment is an example of documentation comment. - Comment type #1
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub - Comment type #2
		
		/*
		 *  This is comment type #3
		 * 
		 *  Data types - 8 existing:-
		 *  4 integer types, 2 floating types, character and boolean
		 *  
		 *  Running the Java program:- 
		 *  javac com/learning/java/Java_Examples.java
		 *  java com.learning.java.Java_Examples
		 */
		System.out.println("Hello World!");
		System.out.println("Hello World!".length());
		System.out.println(new Random().nextInt(10));
		
		/*
		 * Following examples are for variable declarations
		 * 
		 */
		int num = 10;
		byte b = 0;
		short s = 5;
		long l = 560889089;
		
		double d = 5.0;
		float f = 5; // How to declare a float
		
		boolean bool = true;
		char c = 'c';
		
		System.out.println(num);
		System.out.println(b);
		System.out.println(s);
		System.out.println(l);
		System.out.println(d);
		System.out.println(f);
		System.out.println(bool);
		System.out.println(c);
		
		for(int i=0; i<5; i++) {
			System.out.println(i);
		}
	}

}
