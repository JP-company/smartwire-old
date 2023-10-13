package screenshots;

import java.awt.AWTException;
import java.awt.Color;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.Toolkit;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

import file.WireID;

public class ScreenDetection {

	public static boolean Restart() {
	        // 캡쳐할 화면 영역 설정
	        Rectangle screenRect = new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
	        
	        try {
		        // 화면 캡쳐, 저장
		        BufferedImage capture = new Robot().createScreenCapture(screenRect);
		        String filePath = "./screenshots/screenDetection.png";
		        File file = new File(filePath);
		        ImageIO.write(capture, "png", file);
		        
		        // 이미지 불러옴
		        BufferedImage image = ImageIO.read(file);
		        
		        // 색 검출 좌표 설정
		        int[] x = {765, 710, 665, 610};
		        
		        int y = -1;
		        if (WireID.getWireID().contains("sit")) { y = 700; }
		        else if (WireID.getWireID().equals("km1") || WireID.getWireID().equals("km4")) {
		        	y = 695;
		        	x[0] = 755; x[1] = 700; x[2] = 655; x[3] = 610;
		        } else if (WireID.getWireID().contains("km")) { y = 695; }
		        
		        Color[] color = new Color[4];
		        
		        for (int i = 0; i < 4; i++) {
		        	color[i] = new Color(image.getRGB(x[i], y));
		        	if (color[i].getRed() != 0 || color[i].getBlue() != 0 || color[i].getGreen() != 255) {
		        		return false;
		        	}
		        }
		        
	        } catch (AWTException e) { e.printStackTrace(); }
	        catch (IOException e) { 
	        	e.printStackTrace();
	        	System.out.println("뭘까?");
	        } catch (Exception e) { e.printStackTrace(); }
	        
	        return true;
	    }
}




