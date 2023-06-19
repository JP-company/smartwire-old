package firebase;


import java.io.IOException;
import java.net.ConnectException;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

// Operations 기능

// dataUpload(String location, String key_1, String value_1, String coment)
// precondition: location, key_1, value_1 에 각각 서버에 저장할 주소, 키, 값을 받아온다.
// postcondition: 받아온 주소 location에 key:value 형식으로 firebase 서버에 저장한다.
// return: 없음

// 나머지 메서드는 키와 값을 한번에 2개, 3개, 4개씩 저장할 수 있게  오버로딩했다.

public class FirebaseUploadForm {
	
//	private static String firbaseURL = "https://firestore.googleapis.com/v1/projects/sit-wire/databases/(default)/documents/";
	private static String firbaseURL = "https://firestore.googleapis.com/v1/projects/flutterfire-8bfdb/databases/(default)/documents/";
	
	public static void uploadForm(String location, String key_1, String value_1) throws ConnectException, IOException {

		OkHttpClient client = new OkHttpClient();
                                                                                                                                                                                                                                                                                                                                                                                                                                        
        MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(mediaType, 
        				"{\n" +
                        "  \"fields\": {\n" +
                        
                        "    \"" + key_1 + "\": {\n " +
                        "      \"stringValue\": \"" + value_1 + "\" \n " +
                        "    },\n " +
                        
                        "  }\n" +
                        "}"
        		);

        Request request = new Request.Builder()
                .url(firbaseURL + location)
                .patch(body) // post, patch
                .build();

        try (Response response = client.newCall(request).execute()) {
        	if(response.code() == 403) {
        		throw new ConnectException("서버 접근 권한 없음");
        	}
        }
	}
	
	public static void uploadForm(String location, String key_1, String value_1, String key_2, String value_2) throws ConnectException, IOException {
		
		OkHttpClient client = new OkHttpClient();
        
        MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(mediaType, 
        				"{\n" +
                        "  \"fields\": {\n" +
                        
                        "    \"" + key_1 + "\": {\n " +
                        "      \"stringValue\": \"" + value_1 + "\" \n " +
                        "    },\n " +
                        
						"    \"" + key_2 + "\": {\n " +
						"      \"stringValue\": \"" + value_2 + "\" \n " +
						"    },\n " +
                        
                        "  }\n" +
                        "}"
        		);

        Request request = new Request.Builder()
                .url(firbaseURL + location)
                .patch(body) // post, patch
                .build();

        try (Response response = client.newCall(request).execute()) {
        	if(response.code() == 403) {
        		throw new ConnectException("서버 접근 권한 없음");
        	}
        }
	}
	
	public static void uploadForm(String location, String key_1, String value_1, String key_2, String value_2, String key_3, String value_3) throws ConnectException, IOException {
		
		OkHttpClient client = new OkHttpClient();
        
        MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(mediaType, 
        				"{\n" +
                        "  \"fields\": {\n" +
                        
                        "    \"" + key_1 + "\": {\n " +
                        "      \"stringValue\": \"" + value_1 + "\" \n " +
                        "    },\n " +
                        
						"    \"" + key_2 + "\": {\n " +
						"      \"stringValue\": \"" + value_2 + "\" \n " +
						"    },\n " +
						
		                "    \"" + key_3 + "\": {\n " +
		                "      \"stringValue\": \"" + value_3 + "\" \n " +
		                "    },\n " +
                        
                        "  }\n" +
                        "}"
        		);

        Request request = new Request.Builder()
                .url(firbaseURL + location)
                .patch(body) // post, patch
                .build();

        try (Response response = client.newCall(request).execute()) {
        	if(response.code() == 403) {
        		throw new ConnectException("서버 접근 권한 없음");
        	}
        }
	}

	public static void uploadForm(String location, String key_1, String value_1, String key_2, String value_2, String key_3, String value_3, String key_4, String value_4) throws ConnectException, IOException {
		
		OkHttpClient client = new OkHttpClient();
        
        MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(mediaType, 
        				"{\n" +
                        "  \"fields\": {\n" +
                        
                        "    \"" + key_1 + "\": {\n " +
                        "      \"stringValue\": \"" + value_1 + "\" \n " +
                        "    },\n " +
                        
						"    \"" + key_2 + "\": {\n " +
						"      \"stringValue\": \"" + value_2 + "\" \n " +
						"    },\n " +
						
		                "    \"" + key_3 + "\": {\n " +
		                "      \"stringValue\": \"" + value_3 + "\" \n " +
		                "    },\n " +
		                
		                "    \"" + key_4 + "\": {\n " +
		                "      \"stringValue\": \"" + value_4 + "\" \n " +
		                "    },\n " +
                        
                        "  }\n" +
                        "}"
        		);

        Request request = new Request.Builder()
                .url(firbaseURL + location)
                .patch(body) // post, patch
                .build();

        try (Response response = client.newCall(request).execute()) {
        	if(response.code() == 403) {
        		throw new ConnectException("서버 접근 권한 없음");
        	}
        }
	}
	
	
	
public static void uploadForm(String location, String key_1, String value_1, String key_2, String value_2, String key_3, String value_3, String key_4, String value_4, String key_5, String value_5) throws ConnectException, IOException {
		
		OkHttpClient client = new OkHttpClient();
        
        MediaType mediaType = MediaType.parse("application/json; charset=utf-8");
        RequestBody body = RequestBody.create(mediaType, 
        				"{\n" +
                        "  \"fields\": {\n" +
                        
                        "    \"" + key_1 + "\": {\n " +
                        "      \"stringValue\": \"" + value_1 + "\" \n " +
                        "    },\n " +
                        
						"    \"" + key_2 + "\": {\n " +
						"      \"stringValue\": \"" + value_2 + "\" \n " +
						"    },\n " +
						
		                "    \"" + key_3 + "\": {\n " +
		                "      \"stringValue\": \"" + value_3 + "\" \n " +
		                "    },\n " +
		                
		                "    \"" + key_4 + "\": {\n " +
		                "      \"stringValue\": \"" + value_4 + "\" \n " +
		                "    },\n " +
		                
						"    \"" + key_5 + "\": {\n " +
						"      \"stringValue\": \"" + value_5 + "\" \n " +
						"    },\n " +
                        
                        "  }\n" +
                        "}"
        		);

        Request request = new Request.Builder()
                .url(firbaseURL + location)
                .patch(body) // post, patch
                .build();

        try (Response response = client.newCall(request).execute()) {
        	if(response.code() == 403) {
        		throw new ConnectException("서버 접근 권한 없음");
        	}
        }
	}
	
}