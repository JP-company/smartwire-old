package timeFunctions;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.LocalDateTime;
import java.time.Duration;


// Operations 기능

// void setTime()
// precondition: 없음
// postcondition: 
// 			1. currentDate 변수에 23-01-01 형식으로 현재날짜를 저장한다. 서버에 올릴 용도이다.
//			2. currentTime 변수에 08:00:00 형식으로 현재시간을 저장한다. 서버에 올릴 용도이다.
//			3. currentHour 변수에 00 ~ 23 형식으로 현재시간의 시간을 저장한다.
//			4. currentMin 변수에 00 ~ 59 형식으로 현재 시간의 분을 저장한다.
//			5. currentDateForFile 변수에 230101 형식으로 현재 날짜를 저장한다. 스크린샷 파일이름으로 쓰는 용도이다.
//			6. currentTimeForFile 변수에 080000 형식으로 현재 시간을 저장한다. 스크린샷 파일이름으로 쓰는 용도이다.
// return: none

// String getTime(String type)
// precondition: 이 메서드를 호출하기전에 무조건 setTime() 메서드를 호출해서 현재 시간을 업데이트해야 한다.
//				  또한 
// postcondition: 없음
// return: 입력받은 매개 변수 type에 따라 현재 시간에 대한 정보를 반환한다.
//			1. "date" => currentDate 현재 날짜
//			2. "time" => currentTime 현재 시간
//			3. "hour" => currentHour 현재 시간(시)
//			4. "min" => currentMin 현재 시간(분)
//			5. "dateForFile" => currentDateForFile 현재날짜(파일용)
//			6. "timeForFile" => currentTimeForFile 현재시간(파일용)

public class CurrentTime {
	
	private static String currentDate = "";
	private static int currentYear = 0;
	private static int currentMonth = 0;
	private static int currentDay = 0;
	
	private static String currentTime = "";
	private static int currentHour = 0;
	private static int currentMin = 0;
	private static int currentSec = 0;
	
	private static String currentDateForFile = "";
	private static String currentTimeForFile = "";
	
	// 메서드로 시간 추출
	public static void setTime() {
		
		// 현재 날짜
		LocalDate date = LocalDate.now();
		currentDate = date.toString();
		
		// 현재 날짜 (이미지 파일용)
		currentYear = date.getYear();
		currentMonth = date.getMonthValue();
		currentDay = date.getDayOfMonth();
		
		currentDateForFile = String.join("", currentDate.split("-"));
		
		LocalTime time = LocalTime.now();
		
		currentHour = time.getHour();
		currentMin = time.getMinute();
		currentSec = time.getSecond();
		
		String hour = String.valueOf(currentHour);
		String min = String.valueOf(currentMin);
		String sec = String.valueOf(currentSec);
		
		if (currentHour < 10) { hour = "0" + currentHour; }
		if (currentMin < 10) { min = "0" + currentMin; }
		if (currentSec < 10) { sec = "0" + currentSec; }
		
		// 현재 시간
		currentTime = hour + ":" + min + ":" + sec;
		
		
		// 현재 시간 (이미지 파일용)
		currentTimeForFile = hour + min + sec;
	}
	
	
	// 맴버 변수 가져오는 메서드
	public static String getTime(String type) {
		switch(type) {
			case "date":
				return CurrentTime.currentDate;
			case "time":
				return CurrentTime.currentTime;
			case "dateFF":
				return CurrentTime.currentDateForFile;
			case "timeFF":
				return CurrentTime.currentTimeForFile;
//			case "hour":
//				return CurrentTime.currentHour;
//			case "min":
//				return CurrentTime.currentMin;
			default:
				return "";  // 여기에 에러를 만들어서 넘길까? 230316
		}
	}
	
	
	public static int getTimeInt(String type) {
		switch(type) {
			case "hour":
				return CurrentTime.currentHour;
			case "min":
				return CurrentTime.currentMin;
			case "sec":
				return CurrentTime.currentSec;
			case "year":
				return CurrentTime.currentYear;
			case "month":
				return CurrentTime.currentMonth;
			case "day":
				return CurrentTime.currentDay;
			default:
				return -1;  // 여기에 에러를 만들어서 넘길까? 230316
		}
	}
}
