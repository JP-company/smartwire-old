import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:get/get.dart';
import 'package:sitwireapp/firebase_options.dart';
import 'package:sitwireapp/home_page.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:sitwireapp/services/local_notification_service.dart';
import 'package:sitwireapp/login_page.dart';
import 'package:sitwireapp/wire1_page.dart';
import 'package:sitwireapp/wire2_page.dart';


Future<String?> token = FirebaseMessaging.instance.getToken();

Future<void> backgroundHandler(RemoteMessage message) async{
  print(message.data.toString());
  print(message.notification!.title);
}

void main() async{
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform,);
  LocalNotificationService.initialize();
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
      routes: {
        "/" : (context) => LoginPage(),
        "/home" : (context) => HomePage()
      },
      getPages: [
        GetPage(name: "/", page: () => LoginPage()),
        GetPage(name: "/home", page: () => HomePage()),
      ],

    );
  }


}
