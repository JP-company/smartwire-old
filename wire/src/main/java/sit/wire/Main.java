package sit.wire;

import java.awt.AWTException;

// Characters 변수 

// Operations 기능

// 
// precondition:
// postcondition:
// return:

import java.io.IOException;

import data.LogData;
import data.ManagingStatus;
import file.LogFile;
import firebase.FirebaseUpload;
import screenshots.ScreenDetection;
import timeFunctions.CurrentTime;
import timeFunctions.TimeSleep;


public class Main {
	
	private static boolean log = false;
	private static boolean search = false; 

    public static void main(String[] args) throws IOException, AWTException {
    	
    	System.out.println("--------------와이어 알림 프로그램 시작--------------");
    	
    	while (true) {
    		CurrentTime.setTime(); // 현재 시간 설정
    		String[] addedLines = LogFile.addedLines();  // 추가된 로그
    		log = false;
    		search = false;
    		
    		if (addedLines != null) {
    			for (String line : addedLines) {  // 추가된 로그 탐색
    				System.out.println("감지한 로그: " + line);
    				if (!search && line.contains("Nc File:")) { FirebaseUpload.fileInfoUpload(line); search = true;}
    				else if (!search && line.contains("Reset")) { FirebaseUpload.fileInfoUpload(line); search = true;}
    				else if (!search && line.contains("Z:")) {  }
    				
    				for (String logKey : LogData.getLogKeyList()) {  // 추가된 로그에 특정 key포함되어있는지 확인
    					if (!log && line.contains(logKey)) { 
    						FirebaseUpload.logUpload(logKey);
    						log = true;
    					}
    				}
    			}
    		}
    		
    		if (!ManagingStatus.getProcessingStatus() && ScreenDetection.Restart()) {
    			FirebaseUpload.logUpload("가공감지");
    		}
        	TimeSleep.sleep(1);  // 시간 지연
    	}
    }
}