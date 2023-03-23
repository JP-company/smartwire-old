import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:sitwireapp/date_page.dart';
import 'package:sitwireapp/firebase_options.dart';
import 'package:sitwireapp/home_page.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:sitwireapp/login_page.dart';
import 'package:sitwireapp/time_page.dart';


Future<String?> token = FirebaseMessaging.instance.getToken();
Future _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  print("백그라운드 메세지: ${message.messageId}");
}

Future<void> backgroundHandler(RemoteMessage message) async {
  print(message.data.toString());
  print(message.notification!.title);
}

void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform,);
  FirebaseMessaging.onBackgroundMessage(backgroundHandler);
  runApp(MyApp());
}

class MyApp extends StatelessWidget {

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      title: 'Sit wire',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),


      initialRoute: "/",
      getPages: [
        GetPage(name: "/", page: () => LoginPage()),
        GetPage(name: "/home", page: () => HomePage()),
        GetPage(name: "/home/date_page", page: () => DatePage()),
        GetPage(name: "/home/date_page/time_page", page: () => TimePage()),
      ],
    );
  }
}