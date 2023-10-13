package data;

public class ManagingStatus {
	private static boolean processingStatus = false;
	
	
	public static void setStatus(String logKey) {
		if (logKey == "작업 재시작" || logKey == "Nc File:" || logKey == "가공감지") {
			processingStatus = true;
		} else { processingStatus = false; }
	}
	
	public static boolean getProcessingStatus() {
		return processingStatus;
	}
}
