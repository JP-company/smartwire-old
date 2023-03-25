package file;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

// Characters 변수 

// String wireID : 와이어 기계를 식별하는 값이다. ex) SIT_1
// String DIRECTORY : wireID를 저장할 파일의 폴더 이름
// String FILE : wireID를 저장할 파일 이름


// Operations 기능

// void setWireID()
// precondition: 없음
// postcondition: 
//			1. DIRECTORY , FILE 경로에 파일이 없으면 파일을 생성해서 wireID를 파일에 저장한다.
//			2. 파일에서 첫 번째 줄을 불러와 wireID에 저장한다.
// return: 없음

// String getWireID()
// precondition: setWireID()메서드를 무조건 실행해야한다.
// postcondition: 없음
// return: wireID를 반환한다.

public class WireID {
	private static String wireID;
	private static final String DIRECTORY = "setting";
	private static final String FILE = "wireID.txt";
	
	static { 
		try { setWireID(); } catch (IOException e) { e.printStackTrace(); } 
	}
	
	
	private static void setWireID() throws IOException {
		// 폴더 위치, 이름
		String filePath = System.getProperty("user.dir")
				+ File.separator	// Windows('\'), Linux, MAC('/')
				+ DIRECTORY;
		
		File fileDir = new File(filePath);  // 디렉토리 경로
		File file = new File(filePath, FILE);  // 파일 이름
		
		// 파일 존재여부 체크 및 생성
        if (!file.exists()) {
        	fileDir.mkdir();  // 디렉토리 생성
			file.createNewFile();  // 파일 생성
			
			FileWriter fw = new FileWriter(file);
            BufferedWriter writer = new BufferedWriter(fw);
            
            System.out.println("와이어 ID를 입력하세요: ");
            Scanner sc = new Scanner(System.in);
            writer.write(sc.nextLine());
            sc.close();
            writer.close();
        }
        
        ArrayList<String> fileReaded = new ArrayList<>();
    	
		// 파일 불러오기, 한줄씩 저장
    	BufferedReader reader = new BufferedReader(new FileReader(filePath + File.separator + FILE));
    	String str;
    	while ((str = reader.readLine()) != null) {
    		fileReaded.add(str);
    	}
    	reader.close();

    	String[] FileArr = new String[0];
    	FileArr = fileReaded.toArray(FileArr);
    	wireID = FileArr[0];
	}
	
	
	public static String getWireID() {
		return wireID;
	}
}

