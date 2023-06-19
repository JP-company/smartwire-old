package file;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

import firebase.FirebaseUpload;
import timeFunctions.CurrentTime;

//Characters 변수

//int currentLogLength : 현재 로그파일의 길이
//int previousLogLength :  이전 로그파일의 길이
//int addedLogLength : 추가된 로그파일의 길이
//String[] logFileArr : 불러온 로그 파일을 배열에 저장한 것


//Operations 기능
//void checkLogFile()
//precondition : 없음
//postcondition :
//			1. "C:/spmEzCut/LogMessage/" 경로에 현재 날짜에 해당하는 .log파일의 내용을 불러온다.
//			1-1. 해당 파일이 없으면 현재 날짜의 .log파일을 새로 생성한다.
//			2. previousLogLength 변수에 저장되어있는 로그파일 길이(currentLogLength)를 저장한다.
//			3. currentLogLength 변수에 아까 불러온 .log파일의 길이를 저장한다.
//			4. addedLogLength 변수에 이 둘의 차이 즉, 바뀐 log파일의 길이를 저장한다.
//return : 없음

//String[] addedLines()
//precondition : 없음
//postcondition : 없음
//return : 변경된 로그파일을 String[]에 담아 반환한다.


public class LogFile {
	private static int currentLogLength;  // 현재 로그파일 길이
	private static int previousLogLength;  // 이전 로그파일 길이
	private static int addedLogLength;  // 추가된 로그파일 길이
	
	private static String[] logFileArr = new String[0];  // 불러온 로그 파일을 배열에 저장한 것
	
	
	public static String[] addedLines() throws IOException {
		LogFile.checkLogFile();
		
		if (addedLogLength > 0) {
			String strArr[] = new String[addedLogLength];
			
			for (int i = 0; i < addedLogLength; i++) {
				strArr[i] = LogFile.logFileArr[LogFile.logFileArr.length - 1 - i];
			}
			return strArr;
		} else if (addedLogLength < 0) {
			FirebaseUpload.fileInfoUpload();
			return null;
		}
		return null;
	}
	
	
	private static void checkLogFile() throws IOException {  // 로그파일을 확인해서 이전 로그 파일 길이, 현재 로그파일 길이, 변경된 로그파일 길이를 저장한다.
		
		// 파일 위치, 이름
		String filePath = String.format("C:/spmEzCut/LogMessage/%s.log", CurrentTime.getTime("date"));
		File file = new File(filePath);
		
		if (!file.exists()) { file.createNewFile(); }
		
		try {
			ArrayList<String> fileReaded = new ArrayList<>();
	    	
			// 로그 파일 불러오기, 한줄씩 저장
	    	BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream(filePath), "cp949"));
	    	String str;
	    	while ((str = reader.readLine()) != null) {
	    		fileReaded.add(str);
	    	}
	    	
	    	// 배열로 변환
	    	LogFile.logFileArr = new String[0];
	    	LogFile.logFileArr = fileReaded.toArray(LogFile.logFileArr);
	    	
	    	// 이전 로그 파일 길이에 현재 로그 파일 길이 저장
	    	LogFile.previousLogLength = LogFile.currentLogLength;
	    	
	    	// 현재 로그 파일 길이 저장
	    	LogFile.currentLogLength = LogFile.logFileArr.length;
	    	
	    	// 추가된 로그 파일 길이 저장
	    	LogFile.addedLogLength = LogFile.currentLogLength - LogFile.previousLogLength;
	    	
	    	reader.close();
	    	
		} 
		catch (FileNotFoundException fe) { fe.printStackTrace();} 
		catch (ArrayIndexOutOfBoundsException ae) { ae.printStackTrace();}
		catch (Exception e) { e.printStackTrace(); }
	}

}
