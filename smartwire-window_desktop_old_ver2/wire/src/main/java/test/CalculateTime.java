package test;

import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.Duration;
import java.time.LocalDate;

public class CalculateTime {
	
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

	public static void main(String[] args) {
		// 로그 파일에서 시간 추출
		
//		String line = "[I](2023-04-24  06:28:27 pm)작업중 정지 [02:18:09]";
//		
//		String ampm = line.substring(25, 27);
//		
//		// 날짜
//		currentDate = line.substring(4, 14);
//		currentYear = line.substring(4, 8);
//		currentMonth = line.substring(9, 11);
//		currentDay = line.substring(12, 14);
//		
//		// 시간
//		currentTime = line.substring(16, 24);
//		currentHour = line.substring(16, 18);
//		currentMin = line.substring(19, 21);
//		currentSec = line.substring(22, 24);
//		
//		if (ampm.equals("pm")) {
//			int hour = Integer.valueOf(currentHour);
//			hour += 12;
//			currentHour = String.valueOf(hour);
//			currentTime = currentHour + line.substring(18, 24);
//		}
//		
//		currentDateForFile = currentYear + currentMonth + currentDay;
//		currentTimeForFile = currentHour + currentMin + currentSec;
		
		
		
		// 메서드로 시간 설정
		
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
		
		
		
		System.out.println("currentDate: "+currentDate);
		System.out.println("currentYear: "+currentYear);
		System.out.println("currentMonth: "+currentMonth);
		System.out.println("currentDay: "+currentDay);
		System.out.println("currentTime: "+currentTime);
		System.out.println("currentHour: "+currentHour);
		System.out.println("currentMin: "+currentMin);
		System.out.println("currentSec: "+currentSec);
		System.out.println("currentDateForFile: "+currentDateForFile);
		System.out.println("currentTimeForFile: "+currentTimeForFile);
//		System.out.println("ampm: "+ampm);
		
		
		
		
        LocalDateTime startDate = 
        		LocalDateTime.of(currentYear, currentMonth, currentDay, currentHour, currentMin, currentSec);
        
        LocalDateTime endDate = 
        		LocalDateTime.of(2023, 05, 04, 14, 30, 41);

        
        Duration duration = Duration.between(startDate, endDate);

        long seconds = duration.getSeconds();
        int hours = (int)(seconds / 3600);
        long minutes = (seconds % 3600) / 60;
        long remainingSeconds = seconds % 60;

        System.out.println("시작 날짜: " + startDate);
        System.out.println("종료 날짜: " + endDate);
        System.out.println("시간 간격: " + hours + "시간 " + minutes + "분 " + remainingSeconds + "초");
        System.out.println("초: "+ seconds);
    }
        
        
	
}
