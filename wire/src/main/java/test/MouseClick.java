package test;

import java.awt.Robot;
import java.awt.event.InputEvent;

import firebase.FirebaseUpload;


public class MouseClick {

	public static void main(String[] args) {
		try {
			Robot rb = new Robot();
			rb.mouseMove(550, 710);
			rb.mousePress(InputEvent.BUTTON1_DOWN_MASK);
			rb.mouseRelease(InputEvent.BUTTON1_DOWN_MASK);
			
			FirebaseUpload.autoStartDataUpload("Wire Contact Auto Stop");
			
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("[자동 재실행 프로그램] 마우스 클릭에 실패했습니다.");
		}
	}

}
