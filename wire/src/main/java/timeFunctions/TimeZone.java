package timeFunctions;

public class TimeZone {
	private static boolean alarmTime = false;
	private static boolean remoteTime = false;
	
	private static void setAlarmTime() {
		int hour = Integer.valueOf(CurrentTime.getTimeInt("hour"));
		
		alarmTime = false;
		
		if (20 < hour && hour < 24 ) {
			alarmTime = true;
		}
	}
	
	
	private static void setRemoteTime() {
		int hour = Integer.valueOf(CurrentTime.getTimeInt("hour"));
		
		remoteTime = false;
		
		if (20 < hour || hour < 8) {
			remoteTime = true;
		}
	}
	
	
	public static boolean getAlarmTime() {
		setAlarmTime();
		return alarmTime;
	}
	
	public static boolean getRemoteTime() {
		setRemoteTime();
		return remoteTime;
	}
}
