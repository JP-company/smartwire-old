package file;

public class NcFile {
	private static String NcFile = "";
	
	private static void setNcFile(String addedLines) {
		if (WireID.getWireID().contains("km")) { addedLines = addedLines.substring(28); }
		
		if (addedLines.contains("Reset")) { 
			NcFile = "";
		} else {
			NcFile = addedLines.substring(addedLines.indexOf('-') + 1, addedLines.indexOf(".NC") + 3);
		}
		
	}
	
	public static String getNcFile(String addedLines) {
		setNcFile(addedLines);
		return NcFile;
	}
	
	public static String getNcFile() {
		return NcFile;
	}
}
