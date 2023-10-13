package timeFunctions;

// Operations 기능

// void sleep(float sec)
// precondition: 호출시에 몇초 지연시킬지 정하는 sec을 입력받아야 한다.
// postcondition: 입력받은 메개변수 sec초 동안 시간지연을 일으킨다.
// return: 없음

public class TimeSleep { // 시간 지연 메서드 TimeSleep.sleep()

	public static void sleep(float sec) {
        try {
            Thread.sleep((int)(1000 * sec));
        } catch (InterruptedException e) {
            e.printStackTrace(); 
        }
	}
	
	public static void sleep(int sec) {
        try {
            Thread.sleep((int)(1000 * sec));
        } catch (InterruptedException e) {
            e.printStackTrace(); 
        }
	}
}