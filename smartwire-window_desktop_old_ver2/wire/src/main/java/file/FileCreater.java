package file;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class FileCreater {

	
	public static void createFile(String DIRECTORY, String FILE) {
		
		String filePath = System.getProperty("user.dir")
				+ File.separator	// Windows('\'), Linux, MAC('/')
				+ DIRECTORY;
		File fileDir = new File(filePath);
		File file = new File(filePath, FILE);  // 파일 이름
		
		if (!file.exists()) {
			try { 
				fileDir.mkdir();  // 디렉토리 생성
				file.createNewFile();  // 파일 생성 
			} 
			catch (IOException e) { e.printStackTrace(); } 
		}
		
	}
	
	public static void createFile(String filePath) {
		
		File file = new File(filePath);  // 파일 이름
		
		if (!file.exists()) {
			try { file.createNewFile(); }  // 파일 생성  
			catch (IOException e) { e.printStackTrace(); } 
		}
	}
	
	
	public static String[] readFile(String DIRECTORY, String FILE) {
		
		String filePath = System.getProperty("user.dir")
				+ File.separator	// Windows('\'), Linux, MAC('/')
				+ DIRECTORY;
		
		ArrayList<String> fileReaded = new ArrayList<>();
    	
		try {
			// 파일 불러오기, 한줄씩 저장
	    	BufferedReader reader = new BufferedReader(new FileReader(filePath + File.separator + FILE));
	    	String str;
	    	while ((str = reader.readLine()) != null) {
	    		fileReaded.add(str);
	    	}
	    	reader.close();
	    	
		} catch (IOException e) { e.printStackTrace(); }
		
		String[] FileArr = new String[0];
		return fileReaded.toArray(FileArr);
	}
}
