package firebase;

import java.net.ConnectException;
import java.net.UnknownHostException;

import data.DateQueue;
import data.LogData;
import data.ManagingStatus;
import file.NcFile;
import file.WireID;
import screenshots.Screenshots;
import timeFunctions.CurrentTime;


public class FirebaseUpload {
	
	private static String path = "";
	private static String pathLog = "";
	private static String pathPush = "push_server/" + WireID.getWireID();
	private static String pathInfo = "";
	
	static {
		if (WireID.getWireID().contains("km")) { path = "company/km/"; } 
		else if (WireID.getWireID().contains("sit")) { path = "company/sit/"; }
	}
	
	
	public static void fileInfoUpload() {
		try {
			pathInfo = path + WireID.getWireID() + "/FileInfo/" + CurrentTime.getTime("date") + "/" + CurrentTime.getTime("time");
			FirebaseUploadForm.uploadForm(pathInfo, "file", NcFile.getNcFile());
		} catch (UnknownHostException uke) {
			System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + "[파일명 업로드] 인터넷 연결이 불안정합니다.");
		} catch (ConnectException ce) {
			System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + ce.getMessage());
		} catch (Exception e) { e.printStackTrace(); }
	}
	
	public static void fileInfoUpload(String line) {
		try {
			pathInfo = path + WireID.getWireID() + "/FileInfo/" + CurrentTime.getTime("date") + "/" + CurrentTime.getTime("time");
			FirebaseUploadForm.uploadForm(pathInfo, "file", NcFile.getNcFile(line));
		} catch (UnknownHostException uke) {
			System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + "[파일명 업로드] 인터넷 연결이 불안정합니다.");
		} catch (ConnectException ce) {
			System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + ce.getMessage());
		} catch (Exception e) { e.printStackTrace(); }
	}
	
	public static void pushAlarmUpload(String logKey) {
		try {
			FirebaseUploadForm.uploadForm(pathPush, "push", LogData.getLogMap().get(logKey)[0], "time", CurrentTime.getTime("time"), "wireID", WireID.getWireID());
			
		} catch (UnknownHostException uke) {
			System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + "[푸시알림] 인터넷 연결이 불안정합니다.");
		} catch (ConnectException ce) {
			System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + ce.getMessage());
		} catch (Exception e) { e.printStackTrace(); }
	}
	
	
	
	public static void logUpload(String logKey) {
			
			try {
				pathLog = path + WireID.getWireID() + "/Logs/" + CurrentTime.getTime("date") + "/" + CurrentTime.getTime("time");
				
				FirebaseUploadForm.uploadForm(pathLog, "log", LogData.getLogMap().get(logKey)[0], "time", CurrentTime.getTime("time"));
				
				DateQueue.saveDate(CurrentTime.getTime("date"));
				FirebaseUploadForm.uploadForm(path + WireID.getWireID() + "/Logs", "date", DateQueue.getDateData());
				DateQueue.SaveDateData();
				Screenshots.saveScreenshot(logKey);
				
				System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + LogData.getLogMap().get(logKey)[1]);

				ManagingStatus.setStatus(logKey);
				
			} catch (UnknownHostException uke) {
				System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + "[로그 업로드] 인터넷 연결이 불안정합니다.");
			} catch (ConnectException ce) {
				System.out.println(CurrentTime.getTime("date") + " " + CurrentTime.getTime("time") + " " + ce.getMessage());
			} catch (Exception e) { e.printStackTrace(); }
			
		}
}
