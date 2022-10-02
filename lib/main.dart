import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:sitwireapp/detail_pag.dart';
import 'package:sitwireapp/detail_pag1_km.dart';
import 'package:sitwireapp/detail_pag2.dart';
import 'package:sitwireapp/detail_pag2_km.dart';
import 'package:sitwireapp/firebase_options.dart';
import 'package:sitwireapp/home_page.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:sitwireapp/login_page.dart';
import 'package:sitwireapp/wire1_page.dart';
import 'package:sitwireapp/wire2_page.dart';


Future<String?> token = FirebaseMessaging.instance.getToken();
Future _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  print("백그라운드 메세지: ${message.messageId}");
}

Future<void> backgroundHandler(RemoteMessage message) async{
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
        GetPage(name: "/home/wire1page", page: () => Wire1Page()),
        GetPage(name: "/home/wire2page", page: () => Wire2Page()),
        GetPage(name: "/home/wire1page/detail_page1", page: () => DetailPage1()),
        GetPage(name: "/home/wire1page/detail_page2", page: () => DetailPage2()),
        GetPage(name: "/home/wire1page/detail_page1_km", page: () => DetailPage1_KM()),
        GetPage(name: "/home/wire1page/detail_page2_km", page: () => DetailPage2_KM()),
      ],

    );
  }


}
