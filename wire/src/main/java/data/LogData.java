package data;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class LogData {
	
	private static HashMap<String, String[]> logMap = new HashMap<String, String[]>();
	private static ArrayList<String> logKeyList;
	
	static { setLogData(); }

	private static void setLogData() {
		
    	String[] logKey = {		"작업 재시작",							"Nc File:",							
    							"Wire Contact Auto Stop", 			"작업중 30sec 접촉 정지", 
								"M코드정지", 							"작업중 단선",
								"M20-삽입실패", 						"M21-절단실패",
								"M21-잔여와이어 처리실패", 				"와이어 미동작",
								"가공액 미동작",							"자동결선 FEED MOTOR ALARM",
								"자동결선 절단 공정 실패",					"자동결선 잔여 WIRE 처리 실패",
								"자동결선 잔여 WIRE 처리 실패", 				"자동결선 하부 뭉치 WIRE CONTACT",
								"자동결선 상부 센서 WIRE CONTACT", 		"AWF 명령끝날때까지 센서감지",
								"Work Tank Fluid Sensor Abnormal", 	"Auto Door Sensor Abnormal",
								"회수부 와이어 이탈",						"Ready On",
								"Emergency Stop",					"READY Off",
								"Reset",							"작업 끝",
								"작업중 정지",							"Initialization",
								"SPM Device Closed",				"SPM Device DisConnected",
								"SPM Device Open Succeeded",		"가공감지"
    						};


		String[][] logValue = {	{"start_restart", "가공 재시작"},							{"start", "작업 시작"},										
								{"stop_contact", "와이어 접촉"}, 							{"stop_contact_30s", "와이어 30초 접촉"}, 
								{"stop_moff", "M코드 정지"}, 								{"stop_cut", "작업중 와이어 단선"}, 
								{"stop_insert_failure", "자동결선 삽입실패(M20)"}, 			{"stop_cut_failure", "자동결선 절단실패(M21)"},
								{"stop_cleanup_failure", "자동결선 잔여와이어 처리실패(M21)"},	{"stop_wire_notworking", "와이어 미동작"},
								{"stop_liquid_notworking", "가공액 미동작"}, 				{"stop_feed_motor_alarm", "자동결선 FEED MOTOR ALARM!!"},
								{"stop_auto_cut_failure", "자동결선 절단 공정 실패"},			{"stop_auto_cleanup_failure", "자동결선 잔여와이어 처리 실패"},
								{"stop_auto_cleanup_failure", "자동결선 잔여와이어 처리 실패"},	{"stop_lowerpart_contact", "자동결선 하부 뭉치 WIRE CONTACT"},
								{"stop_upperpart_contact", "자동결선 상부 센서 WIRE CONTACT"}, {"stop_awf_sensor", "AWF 명령끝날때까지 센서감지 안됨"},
								{"stop_fluid_sensor", "오일센서 이상 감지"},					{"stop_door_sensor", "자동문센서 이상 감지"},
								{"stop_collect_breakaway", "회수부 와이어 이탈"},				{"ready_on", "Ready On"},
								{"stop_emergency", "비상정지"},							{"ready_off", "READY Off"},
								{"stop_reset", "reset"},								{"stop_finished", "작업 완료"},
								{"stop", "정지"},											{"stop_initialization", "와이어 기계 연결 완료"},
								{"stop_closed", "와이어 기계 전원 종료됨"},						{"stop_disconnected", "와이어 기계 연결 끊어짐"},
								{"stop_open_succeeded", "와이어 기계 전원 켜짐"},				{"start_restart_detected", "가공 감지, 가공 재시작"}
							};
		
		
		for (int i = 0; i < logKey.length; i++) {
			logMap.put(logKey[i], logValue[i]);
    	}
		Set<String> set = logMap.keySet();
		Iterator<String> it = set.iterator();
		
		logKeyList = new ArrayList<String>(set.size());
		while(it.hasNext()){
			logKeyList.add(it.next());
		}
	}
	
	public static ArrayList<String> getLogKeyList() {
		return logKeyList;
	}
	
	public static HashMap<String, String[]> getLogMap() {
		return logMap;
	}
	
}
