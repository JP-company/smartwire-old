package test;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;


public class FileWrite {

	public static void main(String[] args) throws IOException {
		Queue<String> dateData = new LinkedList<String>();
		
		for (int i = 0; i < 10; i++)
			dateData.offer(i + "");
		
		LinkedList<String> tmp = (LinkedList<String>)dateData;
		ListIterator<String> it = tmp.listIterator();
		
		String file = String.format("C:/spmEzCut/LogMessage/hi.txt");
		FileWriter fw = new FileWriter(file);
        BufferedWriter writer = new BufferedWriter(fw);
		
		while(it.hasNext()){
			writer.write(it.next() + "\n");
		}
		
        writer.close();

	}

}
