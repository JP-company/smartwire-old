package test;

import java.time.LocalDateTime;

public class StringToInt {
	
	private static LocalDateTime firstStartDateTime = null;

	public static void main(String[] args) {
		firstStartDateTime = LocalDateTime.of(2023,5,3,20,00,00);
		LocalDateTime s = firstStartDateTime;
		
		System.out.println(firstStartDateTime);
		System.out.println(s);
		
		firstStartDateTime = LocalDateTime.of(2023,6,3,20,00,00);
		
		System.out.println(firstStartDateTime);
		System.out.println(s);

	}

}
