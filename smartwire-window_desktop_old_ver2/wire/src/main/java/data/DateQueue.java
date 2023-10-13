package data;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;

import file.FileCreater;

//import timeFunctions.CurrentTime;

public class DateQueue {

	private static Queue<String> dateData = new LinkedList<String>();
	private static final int MAX_SIZE = 30;
	private static final String DIRECTORY = "setting";
	private static final String FILE = "DateQueue.txt";
	
	static {
		FileCreater.createFile(DIRECTORY, FILE);
		for (String str : FileCreater.readFile(DIRECTORY, FILE)) { saveDate(str); }
	}

	public static void saveDate(String date) {
		if (dateData.peek() == null || !getDateData().contains(date)) { dateData.offer(date); }
		if (dateData.size() > MAX_SIZE) { dateData.remove(); }
	} 
	
	public static String getDateData() {
		
		LinkedList<String> tmp = (LinkedList<String>)dateData;
		ListIterator<String> it = tmp.listIterator();
		
		String str = "";
		
		while(it.hasNext()){ 
			str = str + it.next() + " ";
		}
		
		return str.trim();
	}
	
	public static void SaveDateData() {
		String file = "./setting/DateQueue.txt";
		try{
			FileWriter fw = new FileWriter(file);
	        BufferedWriter writer = new BufferedWriter(fw);
	        
	        LinkedList<String> tmp = (LinkedList<String>)dateData;
			ListIterator<String> it = tmp.listIterator();
			
			String next;
			
			while(it.hasNext()){ 
				next = it.next();
		        if (it.hasNext()) {
		            writer.write(next);
		            writer.newLine();
		        } else {
		            writer.write(next);
		        }
			}
			
			writer.close();
	        
		} catch (IOException e) {e.printStackTrace();}
	}
	
}
