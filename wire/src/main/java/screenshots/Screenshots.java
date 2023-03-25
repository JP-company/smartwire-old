package screenshots;

import java.awt.AWTException;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import data.LogData;
import file.WireID;
import timeFunctions.CurrentTime;

public class Screenshots {
    public static void saveScreenshot(String logKey) {
        try {
        	String fileDirPath = "./screenshots";
        	File fileDir = new File(fileDirPath);  // 디렉토리 경로
        	if(!fileDir.exists()) { fileDir.mkdir(); }
        	
            // 화면 크기 구하기
            Rectangle screenRect = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
            // 로봇 객체생성, 스크린샷 찍기
            BufferedImage image = new Robot().createScreenCapture(screenRect);
            // 이미지 파일로 저장
            String filePath = fileDirPath + "/" + WireID.getWireID() + "_" + CurrentTime.getTime("dateFF") + "_" + CurrentTime.getTime("timeFF") + "_" + LogData.getLogMap().get(logKey)[1] + ".png";
            
            File file = new File(filePath);
            ImageIO.write(image, "png", file);
        } catch (AWTException | IOException ex) {
            System.err.println(ex);
        }
    }
}
