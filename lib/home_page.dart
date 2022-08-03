import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:sitwireapp/alarm_setting.dart';
import 'package:sitwireapp/functions/main_card.dart';
import 'package:sitwireapp/pushnotification_model.dart';
import 'package:sitwireapp/services/local_notification_service.dart';
import 'package:sitwireapp/wire1_page.dart';
import 'package:sitwireapp/wire2_page.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_messaging/firebase_messaging.dart';



Future<void> saveTokenToDatabase(String token) async {

  await FirebaseFirestore.instance
      .collection('users')
      .doc('4')
      .update({
    'tokens': FieldValue.arrayUnion([token]),
  });
}

class HomePage extends StatefulWidget {

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  late final FirebaseMessaging _messaging;
  PushNotification? _notificationInfo;

  void registerNotification() async{
    await Firebase.initializeApp();

    _messaging = FirebaseMessaging.instance;

    NotificationSettings settings = await _messaging.requestPermission(
      alert: true,
      badge: true,
      provisional: false,
      sound: true,
    );
    if (settings.authorizationStatus == AuthorizationStatus.authorized){
      print("User granted the permission");

      FirebaseMessaging.onMessage.listen((RemoteMessage message) {
        PushNotification notification = PushNotification(
          title: message.notification!.title,
          body: message.notification!.body,
        );
        setState(() {
          _notificationInfo = notification;
        });
      });
    }
  }

  storeNotificationToken() async{
    String? token = await FirebaseMessaging.instance.getToken();
    FirebaseFirestore.instance.collection('users').doc('4').set(
        {
          'token': token
        },SetOptions(merge: true));
  }

  checkForInitialMessage() async{
    RemoteMessage? initialMessage = await FirebaseMessaging.instance.getInitialMessage();
    if (initialMessage != null){
      PushNotification notification = PushNotification(
        title: initialMessage.notification!.title,
        body: initialMessage.notification!.body,
      );
      setState(() {
        _notificationInfo = notification;
      });
    }
  }

  @override
  void initState()  {
    // 앱 백그라운드
    FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
      PushNotification notification = PushNotification(
        title: message.notification!.title,
        body: message.notification!.body,
      );
      setState(() {
        _notificationInfo = notification;
      });
    });

    // 일반
    registerNotification();
    // 앱 꺼져있을 때
    checkForInitialMessage();
    // 토큰 저장
    storeNotificationToken();
    super.initState();

  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          title: Text('SIT와이어', style: TextStyle(
              color: Colors.black,
              fontWeight: FontWeight.bold),),
          centerTitle: false,
          elevation: 0.5,
          backgroundColor: Colors.white,
          actions: [
            IconButton(
              icon: Icon(Icons.settings),
              onPressed: (){
                Get.to(AlarmSetting());
              },
              color: Colors.black,
            )
          ],
        ),
        body: ListView(
          children: [Column(
              children: [
                  Padding(
                    padding: EdgeInsets.fromLTRB(0, 30, 0, 0),
                    child: Wire1_sts()
                    ), // 1번 와이어
                  Padding(
                  padding: EdgeInsets.fromLTRB(0, 30, 0, 0),
                  child: StreamBuilder(
                      stream: FirebaseFirestore.instance.collection('wire_2').snapshots(),
                      builder: (BuildContext context,
                          AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot) {
                        if (snapshot.connectionState == ConnectionState.waiting) {
                          return Center(
                            child: CircularProgressIndicator(),
                          );
                        } //렉 방지
                        final docs_pre = snapshot.data!.docs;
                        final last_date = docs_pre.length - 1;
                        final date = docs_pre[last_date]['date'];
                        return StreamBuilder(
                            stream: FirebaseFirestore.instance.collection('wire_2/dates/$date').snapshots(),
                            builder: (BuildContext context,
                                AsyncSnapshot<QuerySnapshot<Map<String, dynamic>>> snapshot){
                              if(snapshot.connectionState == ConnectionState.waiting){
                                return Center(
                                  child: CircularProgressIndicator(),
                                );
                              } //렉 방지
                              final docs = snapshot.data!.docs;
                              final last_sts = docs.length - 1;
                              final onoff = docs[last_sts]['onoff'];
                              final now = docs[last_sts]['now'];
                              if(onoff == 'on'){
                                return ElevatedButton(
                                    onPressed: (){Get.to(Wire2Page());},
                                    style: OutlinedButton.styleFrom(
                                        minimumSize: Size(
                                            300.0,
                                            300.0
                                        ),
                                        backgroundColor: Colors.white,
                                        shadowColor: Color(0xffD5FADC),
                                        elevation: 3,
                                        side: BorderSide(
                                            color: Color(0xff99FA95),
                                            width: 1.0
                                        )
                                    ),
                                    child: Column(children: [
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                                        child: Text('2번 와이어', style: TextStyle(
                                            fontSize: 15.0,
                                            color: Color(0xff4E4E4E)
                                        ),),
                                      ), // 2번 와이어
                                      Image.asset('assets/images/working.gif'), // 움짤
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
                                        child: Text('가동중...',
                                          style: TextStyle(
                                              color:Color(0xff40B137),
                                              fontSize: 16.0,
                                              fontWeight: FontWeight.bold
                                          ),
                                        ),
                                      ), // 가동중
                                      Padding(
                                          padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                                          child: Text('시작 시각: $date $now',
                                            style:
                                            TextStyle(
                                                color:Color(0xff9E9E9E),
                                                fontSize: 16.0
                                            ),
                                          )
                                      ) // 시작 시각
                                    ],
                                    )
                                ); // 가동중 버튼
                              }else{
                                return ElevatedButton(
                                    onPressed: (){Get.to(Wire2Page());},
                                    style: OutlinedButton.styleFrom(
                                        minimumSize: Size(
                                            300.0,
                                            300.0
                                        ),
                                        backgroundColor: Colors.white,
                                        shadowColor: Color(0xffFFB1B1),
                                        elevation: 3,
                                        side: BorderSide(
                                            color: Color(0xffFFB1B1),
                                            width: 1.0
                                        )
                                    ),
                                    child: Column(children: [
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 0, 0, 10),
                                        child: Text('2번 와이어', style: TextStyle(
                                            fontSize: 15.0,
                                            color: Color(0xff4E4E4E)
                                        ),),
                                      ), // 2번 와이어
                                      Image.asset('assets/images/working_stop.jpg'), // 움짤
                                      Padding(
                                        padding: EdgeInsets.fromLTRB(0, 25, 0, 0),
                                        child: Text('가동 정지',
                                          style: TextStyle(
                                              color:Color(0xffEB5B5B),
                                              fontSize: 16.0,
                                              fontWeight: FontWeight.bold
                                          ),
                                        ),
                                      ), // 가동 정지
                                      Padding(
                                          padding: EdgeInsets.fromLTRB(0, 20, 0, 0),
                                          child: Text('정지 시각: $date $now',
                                            style:
                                            TextStyle(
                                                color:Color(0xff9E9E9E),
                                                fontSize: 16.0
                                            ),
                                          )
                                      ), // 정지 시각
                                    ],
                                    )
                                ); // 가동정지 버튼
                              }
                            }
                        );
                      }
                  ),
                ), // 2번 와이어
                ],
              ),
          ]
        ),

    );
  }
}
